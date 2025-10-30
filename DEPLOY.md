# 🚀 Deploy to Streamlit Cloud - Quick Guide

Follow these simple steps to deploy your UI to Streamlit Cloud (takes ~3 minutes):

## Step 1: Push to GitHub

1. **Create a new GitHub repository:**
   - Go to https://github.com/new
   - Name it: `govcon-rag-chatbot`
   - Make it **Public** (required for free Streamlit Cloud)
   - Don't initialize with README (we already have files)
   - Click "Create repository"

2. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit: Apple-inspired GovCon UI"
   git remote add origin https://github.com/YOUR_USERNAME/govcon-rag-chatbot.git
   git push -u origin main
   ```

   Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud:**
   - Visit https://share.streamlit.io/
   - Click "Sign in with GitHub"
   - Authorize Streamlit to access your GitHub account

2. **Deploy your app:**
   - Click "New app" button
   - Select your repository: `YOUR_USERNAME/govcon-rag-chatbot`
   - Main file path: `app.py`
   - Click "Deploy!"

3. **Wait ~2 minutes** for deployment to complete

4. **Done!** You'll get a public URL like:
   `https://YOUR_USERNAME-govcon-rag-chatbot.streamlit.app`

## Alternative: One-Command Deployment

If you have the Streamlit CLI installed:

```bash
streamlit run app.py --server.headless true
```

Then visit the local URL to preview before deploying.

## Troubleshooting

**Issue:** Git push requires authentication
**Solution:** Use a personal access token or SSH key
- GitHub Settings → Developer settings → Personal access tokens

**Issue:** Streamlit Cloud says "App is sleeping"
**Solution:** Just click "Wake up" - free tier apps sleep after inactivity

**Issue:** Want to make the repo private?
**Solution:** Upgrade to Streamlit Cloud Pro ($20/month)

## What You'll See

Once deployed, you'll have a live, public URL showing:
- ✅ Beautiful Apple-inspired UI
- ✅ AI Assistant tab with chat interface
- ✅ Resource Library with 9 sample documents
- ✅ Fully responsive design
- ✅ Mock data (real backend comes next)

## Next Steps After Preview

Once you approve the UI design:
1. Add your Google AI API key
2. Set up Pinecone vector database
3. Upload your 179 documents
4. Connect real Gemini AI backend
5. Deploy production version with secrets

---

Need help? Just ask! 🚀
