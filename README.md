# dallying-with-DALL-E [![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)

Repository for dallying with DALL-E.

 This repository contains Python code, and associated unit tests, which uses the OpenAI API to perform image generation. The code takes the input from the user and generates a response using DALL-E an AI image generator. You just need to provide a description and DALL-E will generate the image.

## To run program

Your OpenAI key is passed to program via an environment variable

```shell
export OPENAI_KEY="Your OpenAI key"
python main.py
```

To generate an OpenAI key browse to [OpenAI API Keys](https://platform.openai.com/account/api-keys) and select "Create new secret key".

## Credits

To generate images you need [DALL-E credits](https://help.openai.com/en/articles/6399305-how-dall-e-credits-work).

## To run unit tests

```shell
pytest
```

## OpenAI API Reference

For more information on the API available see the [OpenAI API Reference Documentation](https://platform.openai.com/docs/api-reference).

