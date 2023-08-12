# dallying-with-DALL-E

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![Bandit](https://github.com/genai-musings/dallying-with-DALL-E/actions/workflows/bandit.yml/badge.svg)](https://github.com/genai-musings/dallying-with-DALL-E/actions/new?category=security)
[![Super-Linter](https://github.com/genai-musings/dallying-with-DALL-E/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![CodeQL](https://github.com/genai-musings/dallying-with-DALL-E/workflows/CodeQL/badge.svg?branch=main)
[![Markdown Links Check](https://github.com/genai-musings/dallying-with-DALL-E/actions/workflows/md-links.yml/badge.svg)](https://github.com/gaurav-nelson/github-action-markdown-link-check)
[![Spell-Checker](https://github.com/genai-musings/dallying-with-DALL-E/actions/workflows/spellcheck.yaml/badge.svg)](https://github.com/rojopolis/spellcheck-github-actions)
[![Unit-Tests](https://github.com/genai-musings/dallying-with-DALL-E/actions/workflows/test.yaml/badge.svg)](https://github.com/actions/setup-python)
[![Code-Coverage](https://github.com/genai-musings/dallying-with-DALL-E/actions/workflows/coverage.yaml/badge.svg)](https://github.com/actions/setup-python)
[![Docker-Build-Push](https://github.com/genai-musings/dallying-with-DALL-E/actions/workflows/docker-build-push.yml/badge.svg)](https://hub.docker.com/)

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

## To build and run an instance of a Docker image locally.

The username and password for Docker Hub are stored as secrets this GitHub repository.

**Note:** To set up the secrets in your GitHub repository, go to the repository page, navigate to the "Settings" tab, and then select "Secrets" from the left menu. Add a secret named DOCKERHUB_USERNAME with the Docker Hub username to be used, and another secret named DOCKERHUB_PASSWORD with the Docker Hub password to be used.

### Build

Build the Docker image.

```shell
docker build -t dallying-with-dall-e .
```

### Run

Run the Docker image as a container.

```shell
export OPENAI_KEY="Your OpenAI key"
docker run -it -e OPENAI_KEY= "Your OpenAI Key" dallying-with-dall-e
```

## To pull and run an instance of the Docker image from Docker Hub

### Pull

```shell
docker pull <dockerhub-username>/dallying-with-dall-e:<tag>
```

Replace <dockerhub-username> with your Docker Hub username and <tag> with the specific tag of the Docker image you want to pull.

### Run

```shell
export OPENAI_KEY="Your OpenAI key"
docker run -it -e OPENAI_KEY= "Your OpenAI Key" <dockerhub-username>/dallying-with-dall-e:<tag>
```

## OpenAI API Reference

For more information on the API available see the [OpenAI API Reference Documentation](https://platform.openai.com/docs/api-reference).

