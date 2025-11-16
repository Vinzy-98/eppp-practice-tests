#!/bin/bash

# Interactive script to deploy EPPP tests to GitHub Pages

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║     EPPP Interactive Tests - GitHub Pages Deployment        ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Error: Not a git repository. Please run this from the Interactive_Tests folder."
    exit 1
fi

echo "This script will help you deploy your tests to GitHub Pages."
echo ""
echo "Prerequisites:"
echo "  ✓ Git repository initialized"
echo "  ✓ All files committed"
echo ""
echo "You will need:"
echo "  1. A GitHub account (create one at https://github.com)"
echo "  2. A new repository created on GitHub"
echo "  3. Your GitHub username"
echo ""

read -p "Do you have a GitHub repository created? (y/n): " has_repo

if [ "$has_repo" != "y" ] && [ "$has_repo" != "Y" ]; then
    echo ""
    echo "Please create a GitHub repository first:"
    echo "  1. Go to https://github.com/new"
    echo "  2. Name it 'eppp-interactive-tests' (or any name)"
    echo "  3. Make it PUBLIC"
    echo "  4. DO NOT initialize with README"
    echo "  5. Click 'Create repository'"
    echo ""
    echo "Then run this script again."
    exit 0
fi

echo ""
read -p "Enter your GitHub username: " github_user

if [ -z "$github_user" ]; then
    echo "❌ Username cannot be empty"
    exit 1
fi

echo ""
read -p "Enter your repository name (default: eppp-interactive-tests): " repo_name
repo_name=${repo_name:-eppp-interactive-tests}

echo ""
echo "Configuration:"
echo "  Username: $github_user"
echo "  Repository: $repo_name"
echo "  URL will be: https://$github_user.github.io/$repo_name/"
echo ""

read -p "Is this correct? (y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "Cancelled."
    exit 0
fi

echo ""
echo "Setting up remote repository..."

# Remove existing remote if it exists
git remote remove origin 2>/dev/null

# Add new remote
git remote add origin "https://github.com/$github_user/$repo_name.git"

echo "✓ Remote added"
echo ""
echo "Pushing to GitHub..."
echo ""
echo "📝 Note: You may be asked for credentials."
echo "   Username: Your GitHub username"
echo "   Password: Use a Personal Access Token (NOT your password)"
echo ""
echo "   To create a token:"
echo "   1. Go to GitHub → Settings → Developer settings"
echo "   2. Personal access tokens → Tokens (classic) → Generate new token"
echo "   3. Select 'repo' scope"
echo "   4. Copy the token and use it as password"
echo ""

read -p "Press Enter to continue with push..."

# Push to GitHub
git branch -M main
if git push -u origin main; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    ✅ SUCCESS!                               ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Your tests have been pushed to GitHub!"
    echo ""
    echo "📋 Next Steps:"
    echo ""
    echo "1. Enable GitHub Pages:"
    echo "   • Go to: https://github.com/$github_user/$repo_name/settings/pages"
    echo "   • Under 'Source', select branch 'main' and folder '/ (root)'"
    echo "   • Click 'Save'"
    echo ""
    echo "2. Wait 1-2 minutes for deployment"
    echo ""
    echo "3. Access your tests at:"
    echo "   🌐 https://$github_user.github.io/$repo_name/"
    echo ""
    echo "4. Share this URL with anyone who needs to take the tests!"
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    echo "Opening GitHub Pages settings in your browser..."
    sleep 2
    open "https://github.com/$github_user/$repo_name/settings/pages"
else
    echo ""
    echo "❌ Push failed. Common issues:"
    echo ""
    echo "1. Authentication failed:"
    echo "   → Make sure you're using a Personal Access Token, not your password"
    echo "   → Create one at: https://github.com/settings/tokens"
    echo ""
    echo "2. Repository doesn't exist:"
    echo "   → Create it at: https://github.com/new"
    echo ""
    echo "3. Remote already exists with different URL:"
    echo "   → Run: git remote set-url origin https://github.com/$github_user/$repo_name.git"
    echo ""
fi
