# Project Documentation

Welcome to our project! This document provides a structured approach to optimizing our development process. It covers key areas essential for maintaining efficiency, clarity, and code quality throughout our project. Specifically, we will discuss:

- Issue Tracking Workflow
- Repository Structure and Organization
- Git Branching Strategy
- Best Practices for Writing Code in the Repository

---

## 1. Issue Tracking Workflow

Managing multiple features, bugs, and enhancements can be challenging. To simplify this, we use a workflow that connects issues directly to branches and automates many repetitive tasks. This makes collaboration smoother and more efficient.

### Strategies for Managing Development Tasks:

1. **Bitbucket-Centric Strategy**:
   - Focuses on using Bitbucket's built-in issue tracking and branching features.

2. **Jira-Centric Strategy**:
   - Uses Jira for issue tracking, integrating with Bitbucket for seamless development tracking.


### Step-by-Step Process:

1. **Create an Issue in git**:
   - **Title**: Reflect the feature you're working on. Example: "Build sentiment model for feedback processing feature."
   - **Description**: Provide details of the task.
   - **Assignee**: Assign to the appropriate teammate.
   - **Kind of Issue**: Choose the issue type (feature, bug, enhancement).
   - **Priority**: Set the priority level.
   - **Attachments**: Include screenshots or visual references if applicable.

   Example Outcome: You receive an issue id, say #1.

2. **Create a Feature Branch**:
   - Name the branch descriptively with the issue id. Example: `1-build-sentiment-model`.

3. **Develop and Commit Your Code**:
   - Commit changes regularly and use specific commit message conventions:
     - **feat**: New Features or Significant Additions
     - **fix**: Bug Fixes or Corrections
     - **refactor**: Code Improvements or Restructuring
     - **chore**: Maintenance Tasks or Minor Updates
     - **doc**: Documentation Updates

4. **Raise a Pull Request (PR)**:
   - Summarize changes and mention `Closes #1` in the PR description.
   - Add a reviewer and select the option to close the branch after merging.

5. **Merge the PR**:
   - The reviewer must test the changes, approve the PR, and merge it into the main branch. Bitbucket will automatically close the related issue.

### Benefits of This Workflow:
- **Track Progress Efficiently**: Link branches and PRs to issues.
- **Organized Branching**: Reflective branch names keep the repository organized.
- **Automatic Issue Closure**: Issues are closed automatically upon PR merge.
- **Clear History**: Maintains a clear, linked chain of changes.
- **Improved Collaboration**: Enhances visibility and collaboration.

## 2. Repository Structure

The following structure is flexible and can be modified based on project requirements:

## Repository Structure

We will follow the below structure for our repository. This structure is flexible and can be modified depending on the specific requirements of the project:
For CI/CD, we are currently using Jenkins. If you choose to use GitHub Actions instead, you can create a workflow folder in the root of the repository to define your CI/CD workflow and inside it create yaml file.

```plaintext
repo-root/
│
├── .jenkins/                        # Jenkins pipeline-related files
│   ├── Jenkinsfile
│   └── manifest.yaml
│
├── config/                          # Configuration files for environments
│   └── dev.env
│
├── data/                            # Data directories
│   ├── raw/
│   └── processed/
│
├── model/                           # Directory for storing model artifacts
│
├── src/                             # Source code of the project
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_preprocessing.py
│   │   └── feature_engineering.py
│   ├── pipeline/                    # Model training and inference pipeline
│   │   ├── __init__.py
│   │   ├── train_model.py
│   │   └── inference.py
│   └── utils/                       # Utility scripts for common functionality
│       ├── __init__.py
│       └── helper_functions.py
│
├── tests/                           # Tests for the project
│   └── __init__.py
│
├── research/                       # Notebooks and experimental code
│   └── test.ipynb
│
├── Dockerfile                       # For containerization
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore file for ignoring unnecessary files
└── README.md                        # Project documentation


```
For further understanding and ease of setup, a template.py file has been provided. Run this script to automatically generate the directory structure as defined above.
A sample Dockerfile and a sample jenkins.dev file have been provided in the repository. These can be modified as per your project’s requirements.
## 3. Git Branching Strategy

### Branch Creation:

- **Feature Branches**: Create a new branch for each feature or task. Example: `1-build-sentiment-model`.
- **Multiple Branches**: Work on multiple branches based on tasks.

### Push Changes:

- **Regular Pushes**: Push changes to remote feature branches regularly.

### Pull Requests (PRs):

- **Raising PRs**: Raise a PR to merge feature branches into the main branch. Include a summary of changes and link to issues.
- **Post-Merge Tasks**: Create new branches for missed updates.

### Branching for New Issues:

- **Separate Branches**: Create a separate branch for each issue from the main branch.

---

## 4. Best Practices for Writing Code in the Repo

### Code Organization and Modularity:

- **Follow the Structure**: Keep code organized per the outlined structure.
- **Modularization**: Break down code into reusable modules.
- **Use `__init__.py`**: Ensure all directories containing Python scripts include an `__init__.py` file.

### Code Quality and Readability:

- **Follow PEP 8**: Adhere to PEP 8 standards.
- **Inline Documentation**: Add docstrings and comments to explain the code.

### Version Control:

- **Follow Commit Message Conventions**: Use clear and consistent commit messages.
- **Use .gitignore**: Exclude unnecessary files and directories.

### Dependency Management:

- **Use requirements.txt**: Maintain a `requirements.txt` file for dependencies.
- **Use Virtual Environments**: Manage dependencies with virtual environments.

### Environment Management:

- **Configuration Files**: Store configuration files in the `config/` directory.
- **Environment Variables**: Use environment variables for sensitive information.

### Documentation:

- **Keep README.md Updated**: Ensure the README.md file is up-to-date with project details.

### Dockerization:

- **Dockerfile Best Practices**: Optimize the Dockerfile for containerization.
- **Multi-Stage Builds**: Use multi-stage builds in the Dockerfile.

### Research and Experiments:

- **Isolate Experimental Code**: Use the `research/` directory for experimental code.
- **Document Experiments**: Document findings in the `research/` directory.

---

By following this documentation, we can streamline our development process, keep our repository organized, and enhance team collaboration.


