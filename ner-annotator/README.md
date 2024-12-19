# NER Annotator Custom

NER Annotator Custom is build on top of [NER Annotator](https://github.com/tecoholic/ner-annotator). 
I changed the source code as per my custom requirements.



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

### Developing the desktop application

The desktop applications have been created using [Tauri](https://tauri.studio).

```sh
yarn tauri:serve
```

To build the final binaries run

```sh
yarn tauri:build
```

