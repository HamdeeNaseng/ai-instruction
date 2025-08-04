#!/bin/bash
# Git Dual Repository Management Script
# This script helps manage pushing to both GitHub and GitLab repositories

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔄 Git Dual Repository Management${NC}"
echo "=================================="

# Function to check git status
check_status() {
    echo -e "\n${YELLOW}📊 Current Git Status:${NC}"
    git status --short
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Repository is clean${NC}"
    else
        echo -e "${RED}❌ There are uncommitted changes${NC}"
        exit 1
    fi
}

# Function to show remote configuration
show_remotes() {
    echo -e "\n${YELLOW}🌐 Remote Configuration:${NC}"
    git remote -v
}

# Function to push to both repositories
push_to_both() {
    local branch=${1:-main}
    
    echo -e "\n${YELLOW}🚀 Pushing to both repositories...${NC}"
    echo -e "Branch: ${BLUE}$branch${NC}"
    
    # Push to origin (which now pushes to both GitLab and GitHub)
    echo -e "\n${YELLOW}📤 Pushing to origin (both GitLab and GitHub):${NC}"
    git push origin $branch
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Successfully pushed to both repositories!${NC}"
    else
        echo -e "${RED}❌ Push failed!${NC}"
        exit 1
    fi
}

# Function to sync from GitLab (primary)
sync_from_gitlab() {
    echo -e "\n${YELLOW}⬇️  Syncing from GitLab (primary repository):${NC}"
    git fetch origin
    git pull origin main
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Successfully synced from GitLab${NC}"
    else
        echo -e "${RED}❌ Sync failed!${NC}"
        exit 1
    fi
}

# Function to create and push a new branch to both repos
create_and_push_branch() {
    local branch_name=$1
    
    if [ -z "$branch_name" ]; then
        echo -e "${RED}❌ Please provide a branch name${NC}"
        exit 1
    fi
    
    echo -e "\n${YELLOW}🌿 Creating and pushing new branch: ${BLUE}$branch_name${NC}"
    
    # Create and switch to new branch
    git checkout -b $branch_name
    
    # Push to both repositories
    git push origin $branch_name
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Branch '$branch_name' created and pushed to both repositories!${NC}"
    else
        echo -e "${RED}❌ Failed to push branch!${NC}"
        exit 1
    fi
}

# Main script logic
case "$1" in
    "status")
        check_status
        show_remotes
        ;;
    "push")
        check_status
        push_to_both $2
        ;;
    "sync")
        sync_from_gitlab
        ;;
    "branch")
        create_and_push_branch $2
        ;;
    "remotes")
        show_remotes
        ;;
    *)
        echo -e "${YELLOW}Usage:${NC}"
        echo "  $0 status          - Show git status and remotes"
        echo "  $0 push [branch]   - Push to both repositories (default: main)"
        echo "  $0 sync            - Sync from GitLab (primary repo)"
        echo "  $0 branch <name>   - Create and push new branch to both repos"
        echo "  $0 remotes         - Show remote configuration"
        echo ""
        echo -e "${YELLOW}Examples:${NC}"
        echo "  $0 push main       - Push main branch to both repos"
        echo "  $0 branch feature/new-demo - Create and push new feature branch"
        echo "  $0 sync            - Pull latest changes from GitLab"
        ;;
esac
