import requests
import json
import datetime
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from demo_exp1.prompt import get_initial_prompt, get_update_prompt
import ast
from server_gpt import predict

GPT_URL = "127.0.0.1"
GPT_PORT = 7777

def add_start_end_index(input_text, spans):

    input_text = input_text

    output_dict = dict()
    output_dict["classes"] = [
        "UNFAMILIAR",
        "SOMEWHAT FAMILIAR"
    ]
    output_dict["annotations"] = [[input_text, dict()]]

    entities_list = list()
    input_text = input_text.lower()
    for span in spans:
        familiarity = span["familiarity"]
        start_index = input_text.find(span["CSI"].lower())
        
        if start_index == -1:
            entities_list.append([-1,-1, familiarity.upper()])
        else:
            end_index = start_index + len(span["CSI"]) - 1
            entities_list.append([start_index, end_index, familiarity.upper()])

    output_dict['annotations'][0][1]["entities"] = entities_list
    return output_dict

def filter_on_familiarity(response):
    spans = response["spans"]
    if(spans != "None"):
        response_filtered_spans = [span for span in spans if span['familiarity'].lower() != 'familiar']
        return response_filtered_spans
    else:
        return []
        

def filter_and_add_start_end_indices(input_text, response):
    response_filtered_spans = filter_on_familiarity(response)
    response_add_start_end_index = add_start_end_index(input_text, response_filtered_spans)
    return response_add_start_end_index

def get_response_initial_prompt(input_text, country, region, age_group, 
                                political_awareness, education_level, literature_preference, food_cuisine,
                                messages, previous):
    
    prompt = get_initial_prompt(input_text, country, region, age_group, 
                                political_awareness, education_level, literature_preference, food_cuisine, 
                                previous)
  
    messages.append({"role": "user", "content": prompt})
    payload = {
        'messages': messages
    }
    
    print(f"Identifying CSIs from the given text...")
    response = predict(payload)
    messages.append({"role":"assistant", "content": str(response)})    
    return response, messages

def get_spans(initial_tokens):
    spans = {'FAMILIAR': [], 'SOMEWHAT FAMILIAR': [], 'UNFAMILIAR': []}
    for init_token in initial_tokens:
        label = init_token["label"]
        tokens = []
        for token in init_token["tokens"]:
            tokens.append(token["text"])
        spans[label].append(' '.join(tokens))
    return spans

def get_added_removed_spans(sp1, sp2):
    added = {}
    removed = {}

    for familiarity in sp1.keys():
        set1 = set(sp1[familiarity])
        set2 = set(sp2[familiarity])
        added[familiarity] = list(set2 - set1)
        removed[familiarity] = list(set1 - set2)
    
    for key, values in removed.items():
        if(values != []):
            for value in values:
                added['FAMILIAR'].append(value)

    return added

def get_response_update_prompt(annotations_initial, annotations_updated, messages):
    initial_spans = get_spans(annotations_initial)
    updated_spans = get_spans(annotations_updated)
    difference_spans = get_added_removed_spans(initial_spans, updated_spans)
    
    prompt = get_update_prompt(difference_spans)
    messages.append({"role": "user", "content": prompt})
    return messages

def get_explanations(response):
    filtered_spans = filter_on_familiarity(response)
    explanations = []

    for span in filtered_spans:
        explanations.append({"CSI": span['CSI'], "explanation": span['explanation']})

    return explanations

def get_response_from_backend_exp1(query_parameters):

    type_ = query_parameters['type']

    if('text' not in query_parameters.keys()):
        url_to_text_path = os.path.join(parent_dir, 'url_to_text.json')
        with open(url_to_text_path, 'r') as file:
            url_to_text = json.load(file)
        text = url_to_text[query_parameters['url']]
    else:
        text = query_parameters['text']

    country = query_parameters['country']
    age_group = query_parameters['age_group']
    region = query_parameters['region']
    messages = query_parameters['messages']

    political_awareness = query_parameters['political_awareness']
    education_level = query_parameters['education_level']
    literature_preference = query_parameters['literature_preference']
    food_cuisine = query_parameters['food_cuisine']

    if(isinstance(messages, list) == False):
        messages = list(ast.literal_eval(messages))

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    if(type_ == 'fresh'):
        response, messages = get_response_initial_prompt(text, country, region, age_group, 
                                                         political_awareness, education_level, literature_preference, food_cuisine,
                                                         messages, previous=False)
        query_parameters['annotations_response'] = filter_and_add_start_end_indices(text, response)
        query_parameters['explanations'] = get_explanations(response)
        query_parameters['messages'] = messages
        # print(query_parameters)
        # json.dump(query_parameters, open(f'outputs/{type_}_{country}_{age_group}_{region}_{timestamp}.json','w'), indent=4)
    
    elif(type_ == 'old'):
        response, messages = get_response_initial_prompt(text, country, region, age_group, 
                                                         political_awareness, education_level, literature_preference, food_cuisine,
                                                         messages, previous=True)
        query_parameters['annotations_response'] = filter_and_add_start_end_indices(text, response)
        query_parameters['messages'] = messages
        query_parameters['explanations'] = get_explanations(response)
        # print(query_parameters)
        # json.dump(query_parameters, open(f'outputs/{type_}_{country}_{age_group}_{region}_{timestamp}.json','w'), indent=4)
   
    elif(type_ == 'save_info'):
        annotations_initial = query_parameters['annotations_updated']['token_block_initial']
        annotations_updated = query_parameters['annotations_updated']['token_block_body']
        messages = get_response_update_prompt(annotations_initial, annotations_updated, messages)
        query_parameters['messages'] = messages
        # print(query_parameters)
        # json.dump(query_parameters, open(f'outputs/{type_}_{country}_{age_group}_{region}_{timestamp}.json','w'), indent=4)

    return query_parameters