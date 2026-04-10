# Publishing Your Own Skills

WLAH uses a decentralized, Git-based distribution model. This guide explains how to structure and publish your own skills so they can be installed with a single command.

## 1. The Core Requirement: `SKILL.md`

Every skill must have a `SKILL.md` file. The CLI looks for this file to understand what the skill is and how to use it.

### File Structure
Place your skill in a directory that makes sense. Common patterns are:
- `skills/<skill-name>/SKILL.md`
- `.agents/skills/<skill-name>/SKILL.md` (Best for project-specific agents)

### Anatomoy of `SKILL.md`
Your file **must** start with YAML frontmatter:

```markdown
---
name: my-awesome-skill
description: A brief summary of what this skill does.
---

# My Awesome Skill

Detailed instructions for the AI on how to execute this skill.
```

## 2. Publishing to GitHub

1. **Create a Public Repo**: Host your code on GitHub or any public Git provider.
2. **Push Your Skills**: Ensure your `SKILL.md` and any supporting scripts are in the repo.
3. **That's it**: Your skill is now "published." There is no central registry to submit to.

## 3. How Others Can Install It

Once your repo is public, anyone can install your skill using the `npx skills` command:

```bash
npx skills add <github-username>/<repo-name> --skill <skill-name>
```

### Example
If your username is `coder` and your repo is `my-tools`, and you have a skill named `debugger`:
```bash
npx skills add coder/my-tools --skill debugger
```

## 4. Best Practices

- **Atomic Skills**: Keep skills focused on one specific task.
- **Provide Examples**: Include usage examples in your `README.md`.
- **Include Scripts**: If your skill needs custom logic (e.g., Python scripts for analysis), include them in the same directory and reference them in `SKILL.md`.
- **Telemetry**: Successfull installs are tracked by [skills.sh](https://skills.sh). If your skill gets popular, it will automatically appear in the global registry based on usage.

## 5. Testing Locally
Before sharing, test your skill by copying it into a local project's `.agents/skills/` folder and seeing if your AI agent picks it up.
