# Git Dual Repository Setup

This repository is configured to push to both GitLab (primary) and GitHub (mirror) simultaneously.

## 🌐 Repository Configuration

- **Primary Repository (GitLab)**: https://gitlab.intermedisoft.com/research/ai-instruction.git
- **Mirror Repository (GitHub)**: https://github.com/HamdeeNaseng/ai-instruction.git

## 🔧 Current Setup

The repository is configured with the following remotes:

```bash
origin  https://gitlab.intermedisoft.com/research/ai-instruction.git (fetch)
origin  https://gitlab.intermedisoft.com/research/ai-instruction.git (push)
origin  https://github.com/HamdeeNaseng/ai-instruction.git (push)
gitlab  https://gitlab.intermedisoft.com/research/ai-instruction.git (fetch)
gitlab  https://gitlab.intermedisoft.com/research/ai-instruction.git (push)
github  https://github.com/HamdeeNaseng/ai-instruction.git (fetch)
github  https://github.com/HamdeeNaseng/ai-instruction.git (push)
```

## 🚀 Usage

### Push to Both Repositories

```bash
# Push current branch to both repositories
git push origin

# Push specific branch to both repositories
git push origin main
git push origin feature-branch
```

### Individual Repository Operations

```bash
# Push only to GitLab
git push gitlab main

# Push only to GitHub
git push github main

# Fetch from GitLab (primary)
git pull origin main

# Fetch from GitHub
git pull github main
```

### Using the Management Script

A helper script `git-dual-repo.sh` is provided for convenient operations:

```bash
# Make script executable (Linux/Mac)
chmod +x git-dual-repo.sh

# Show status and remotes
./git-dual-repo.sh status

# Push to both repositories
./git-dual-repo.sh push

# Push specific branch
./git-dual-repo.sh push develop

# Sync from primary (GitLab)
./git-dual-repo.sh sync

# Create and push new branch to both repos
./git-dual-repo.sh branch feature/new-feature

# Show remote configuration
./git-dual-repo.sh remotes
```

### PowerShell Commands (Windows)

For PowerShell users, here are equivalent commands:

```powershell
# Push to both repositories
git push origin

# Check remote configuration
git remote -v

# Sync from GitLab
git pull origin main

# Push specific branch
git push origin feature-branch
```

## 🔄 Workflow Recommendations

### Daily Development Workflow

1. **Start of day**: Sync from primary repository
   ```bash
   git pull origin main
   ```

2. **Make changes**: Work on your features/fixes
   ```bash
   git add .
   git commit -m "feat: your feature description"
   ```

3. **Push changes**: Push to both repositories
   ```bash
   git push origin
   ```

### Feature Branch Workflow

1. **Create feature branch**:
   ```bash
   git checkout -b feature/your-feature
   git push origin feature/your-feature  # Pushes to both repos
   ```

2. **Work and commit**:
   ```bash
   git add .
   git commit -m "feat: implement your feature"
   git push origin  # Pushes to both repos
   ```

3. **Merge back**:
   ```bash
   git checkout main
   git merge feature/your-feature
   git push origin  # Pushes to both repos
   ```

## 🎯 Best Practices

### Repository Roles

- **GitLab (Primary)**: Main development, CI/CD, internal collaboration
- **GitHub (Mirror)**: Public visibility, external contributions, documentation

### Conflict Resolution

If conflicts arise between repositories:

1. **GitLab is the source of truth** - always resolve conflicts by favoring GitLab
2. **Force push to GitHub if needed**:
   ```bash
   git push github main --force
   ```

### Branch Management

- Keep both repositories in sync for main branches
- Feature branches can be pushed to both or just primary as needed
- Delete merged branches from both repositories:
  ```bash
  git push origin --delete feature-branch
  git push github --delete feature-branch
  ```

## ⚙️ Advanced Configuration

### Adding New Remote URLs

If you need to add more repositories:

```bash
# Add another push URL to origin
git remote set-url --add --push origin https://another-repo.git
```

### Removing Dual Push Setup

To revert to single repository:

```bash
# Remove all push URLs
git remote set-url --delete --push origin https://github.com/HamdeeNaseng/ai-instruction.git

# Reset to single push URL
git remote set-url origin https://gitlab.intermedisoft.com/research/ai-instruction.git
```

## 🔍 Troubleshooting

### Common Issues

1. **Authentication Errors**:
   - Ensure you have access to both repositories
   - Check SSH keys or personal access tokens for both platforms

2. **Push Failures**:
   - One repository might be ahead of the other
   - Sync both repositories manually:
     ```bash
     git pull gitlab main
     git push github main
     ```

3. **Different Branch Names**:
   - GitHub uses `main`, GitLab might use `master` or `main`
   - Ensure both repositories use the same default branch name

### Verification Commands

```bash
# Check if both remotes are accessible
git ls-remote origin
git ls-remote gitlab
git ls-remote github

# Verify current branch tracking
git branch -vv

# Check for differences between remotes
git fetch --all
git log --oneline --graph --all
```

## 📝 Notes

- This setup pushes to both repositories simultaneously with `git push origin`
- GitLab is treated as the primary repository for fetching/pulling
- Both repositories should maintain the same branch structure for consistency
- The `.github/` directory contains GitHub-specific workflows and templates
- Consider adding GitLab CI configuration if needed

---

This dual repository setup ensures your code is always synchronized between your internal GitLab and public GitHub repositories! 🚀
