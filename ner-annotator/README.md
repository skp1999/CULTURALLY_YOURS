# NER Annotator Custom

A customizable Named Entity Recognition (NER) annotation tool built with Vue.js. This tool allows users to annotate text with entity labels and compare initial and updated annotations.

## Usage

1. **Start Page**: Upload or input text for annotation
2. **Annotation Page**: 
   - Select text to create entity annotations
   - View and edit existing annotations
   - Track added and removed spans
   - View explanations for annotations
3. **Comparison Page**: Compare initial and updated annotations side by side


## Development

### Requirements

1. Node JS 14.x
2. Yarn Package Manager
3. Rust (for building desktop versions)

### Running it locally for development

1. Open another terminal and start the server for the UI

```sh
yarn
yarn serve
```

Now go to [http://localhost:8080/ner-annotator/](http://localhost:8080/ner-annotator/)

