---
icon: simple/markdown
---

# Markdown guide for FocusFlow

This page explains the Markdown features used in the project documentation and shows how to write clear, structured docs for the FocusFlow backend.

## 1. Headings

Use headings to organize documentation from general overview to detailed sections.

```md
# Project title
## Overview
### Requirements
#### Installation
```

## 2. Text formatting

Markdown supports emphasis and code styling for better readability.

```md
**Bold text**
*Italic text*
`inline code`
***Important note***
```

## 3. Lists

Use lists to describe steps, features, or requirements.

### Bullet list

```md
- FastAPI application
- Centralized configuration
- API routing
```

### Numbered list

```md
1. Create a virtual environment
2. Install dependencies
3. Run the server
```

## 4. Links and references

Use links to connect documentation to related files or external resources.

```md
[README](../README.md)
[FastAPI docs](https://fastapi.tiangolo.com/)
```

## 5. Code blocks

Code blocks are ideal for showing commands, configuration examples, and snippets.

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

You can also add language hints for better highlighting:

```python
from fastapi import FastAPI

app = FastAPI()
```

## 6. Blockquotes

Use blockquotes for notes, warnings, or callouts.

```md
> Tip: Keep documentation concise and practical.
```

## 7. Tables

Tables are useful for comparing options or summarizing setup details.

```md
| Item | Description |
|------|-------------|
| FastAPI | Web framework |
| Pydantic | Settings and validation |
| Uvicorn | ASGI server |
```

## 8. Task lists

Task lists work well for checklists and development progress.

```md
- [x] Set up project structure
- [x] Add API route
- [ ] Add database integration
```

## 9. Useful documentation patterns for this project

When writing docs for FocusFlow, keep sections focused on:

- project overview
- setup and dependencies
- API behavior
- deployment notes
- architecture decisions

### Example section

```md
## Quick start

1. Create a virtual environment
2. Install dependencies
3. Run the development server
4. Visit the API documentation
```

## 10. Best practices

- Keep headings short and descriptive
- Use fenced code blocks for examples
- Prefer concise sentences over long paragraphs
- Link to the relevant source files when helpful
- Update documentation whenever the app behavior changes
