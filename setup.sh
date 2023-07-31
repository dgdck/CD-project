
# Setup deploy keys for GitHub
# Start the ssh-agent in the background
eval "$(ssh-agent -s)"
# Add identity to ssh-agent
ssh-add ~/.ssh/winc
# Connect to GitHub
ssh -T git@github.com

# Do something extremely useful for continous deployment
git pull
