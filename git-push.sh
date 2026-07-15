#!/bin/bash

# Exit immediately if any command fails
set -e

# 1. Verify this is a Git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "❌ Error: This directory is not a Git repository."
    exit 1
fi

# 2. Check for changes to commit
if git diff --quiet && git diff --cached --quiet; then
    echo "ℹ️ No changes detected. Nothing to push."
    exit 0
fi

# 3. Get the current branch name dynamically
CURRENT_BRANCH=$(git branch --show-current)

# 4. Stage all changes (tracked and untracked)
echo "📦 Staging all modifications..."
git add .

# 5. Prompt user for a commit message
echo "💬 Enter your commit message (or press Enter for 'Auto-commit updates'):"
read -r COMMIT_MSG

if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="Auto-commit updates: $(date +'%Y-%m-%d %H:%M:%S')"
fi

# 6. Commit the changes
echo "💾 Committing changes..."
git commit -m "$COMMIT_MSG"

# 7. Push to the remote repository
echo "🚀 Pushing branch '$CURRENT_BRANCH' to origin..."

# Using --set-upstream to safeguard the first-time push of new branches
if git push -u origin "$CURRENT_BRANCH"; then
    echo "✅ Successfully pushed to GitHub!"
else
    echo "❌ Push failed. Check your network or permissions."
    exit 1
fi
