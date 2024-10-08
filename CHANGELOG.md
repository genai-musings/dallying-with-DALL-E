# Dallying With DALL-E

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.8.0] - 2024-09-29

- [ADDED] Upgraded to latest version of OpenAI API
- [FIXED] Unit Tests
- [FIXED] Bug in saving generated image for use with unit tests

## [1.7.0] - 2024-09-08

- [ADDED] Safety GitHub Action workflow to check Python dependencies for known security vulnerabilities.
- [ADDED] Trivy scan of the Docker image for vulnerabilities
- [FIXED] Vulnerabilities in docker images reported by Trivy
- [CHANGED] Updates to README.md

## [1.6.4] - 2023-10-22

- [FIXED] Bug in Dockerfile by adding folder to store images generated

## [1.6.3] - 2023-10-20

- [ADDED] Documentation in the form of code comments.

## [1.6.2] - 2023-10-19

- [ADDED] Ensured docker image pushed to Docker Hub before README.md

## [1.6.1] - 2023-10-17

- [CHANGED] Updates to README.md
- [CHANGED] Updates to Dockerfile maintainers
- [ADDED] CODEOWNERS

## [1.6.0] - 2023-10-09

- [ADDED] GitHub Action Linting to Super-Linter workflow
- [ADDED] Shell Script Linting to Super-Linter workflow
- [ADDED] Maintainer and description labels to Dockerfile
- [ADDED] Workflow to automatically update Image description on Docker Hub with contents of README.md
- [CHANGED] Updates to README.md.

## [1.5.3] - 2023-08-12

- [ADDED] Docker Build Push badge to README.md.

## [1.5.2] - 2023-08-04

- [FIXED] 403 error when validating OpenAI Keys page link from Markdown link checking action.
- [FIXED] Code scanning issue - Requests call with timeout set to None.

## [1.5.1] - 2023-08-03

- [FIXED] Issue with case of docker repository name.

## [1.5.0] - 2023-08-03

- [ADDED] Dockerized application.

## [1.4.0] - 2023-08-02

- [ADDED] CodeQL Security Action
- [ADDED] Bandit Security Action
- [ADDED] Code Coverage Action
- [ADDED] Dependabot check

## [1.3.5] - 2023-06-24

- [FIXED] Permissions error in greetings.yml

## [1.3.4] - 2023-06-21

- [CHANGED] Fine tuned markdown link checker GitHub action triggers

## [1.3.3] - 2023-06-19

- [ADDED] Markdown link checker GitHub action
- [ADDED] JSON validation via SuperLinter
- [CHANGED] Replaced pylint and yamllint workflows with SuperLinter workflow

## [1.3.2] - 2023-06-11

- [ADDED] GitHub Issue & PR templates plus associated actions

## [1.3.1] - 2023-06-09

- [ADDED] License

## [1.3.0] - 2023-06-01

- [CHANGED] Refactored Actions
- [ADDED] yamllint action
- [ADDED] pylint action

## [1.2.1] - 2023-05-31

- [CHANGED] Moved unit tests to tests folder

## [1.2.0] - 2023-05-31

- [ADDED] CONTRIBUTING.md
- [ADDED] GitHub action to check markdown spelling
- [CHANGED] GitHub action to run unit tests for pull requests

## [1.1.0] - 2023-05-24

- [ADDED] CHANGELOG.md

## [1.0.0] - 2023-05-23

- [ADDED] Initial Release
