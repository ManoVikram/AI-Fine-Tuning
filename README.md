# Fine Tuning an AI Model

Fine-tuning an AI model to help it adapt to the style and tone and structure of the responses / answers you expect out of it.

## Install the Necessary Packages

All the necessary Python pacakges are added to the [requirements.txt](/services/requirements.txt) file. Run the below command to install all the packages from this file.

```bash
pip3 install -r requirements.txt
```

The below command installs the necessary Go gRPC packages.

```bash
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

Add the installed Go protoc-gen-go package to PATH

```bash
export PATH="$PATH:$(go env GOPATH)/bin"
```

## Generate the gRPC Files

Run the below command from the /backend folder to generate the Python gRPC files.

```bash
python3 -m grpc_tools.protoc -I./proto --python_out=./services/proto --grpc_python_out=./services/proto ./proto/service.proto
```

Run the below command from the /backend folder to generate the Go gRPC files.

```bash
protoc --proto_path=./proto --go_out=./api/proto --go_opt=paths=source_relative --go-grpc_out=./api/proto --go-grpc_opt=paths=source_relative ./proto/service.proto
```

## API Usage

### Request

```bash
curl --location 'http://localhost:8080/api/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query": "What is Hugging Face and why should I care about it?"
}'
```

### Response

```bash
{"answer":"Hugging Face is a leading platform for machine learning, particularly known for its natural language processing (NLP) capabilities. Here's why you should care about it:\n\n1. **Model Hub**: Hugging Face provides a massive repository of pre-trained machine learning models (over 100,000) that you can easily download and use. This means you don't have to train models from scratch.\n\n2. **Ease of Use**: Their libraries (like Transformers) allow developers to implement complex models with just a few lines of code. For example, loading a BERT model might look like this:\n   ```python\n   from transformers import pipeline\n   sentiment_analysis = pipeline('sentiment-analysis')\n   ```\n\n3. **Community**: It's not just a library, but a community of researchers and developers sharing models, datasets, and best practices.\n\n4. **Versatility**: Supports multiple tasks - text classification, translation, image processing, code generation, and more.\n\n5. **Integration**: Works seamlessly with popular frameworks like TensorFlow and PyTorch.\n\n6. **Accessibility**: Lowering the barrier to entry for AI, allowing non-experts to leverage powerful machine learning capabilities.\n\nIn short, Hugging Face is a game-changer for anyone working with AI, making advanced machine learning more accessible and practical."}
```