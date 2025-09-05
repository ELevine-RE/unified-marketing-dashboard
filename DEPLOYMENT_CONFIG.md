# 🚀 Streamlit Cloud Deployment Configuration

## 📋 **Repository Details**
- **Repository Name:** `unified-marketing-dashboard`
- **Full Repository:** `ELevine-RE/unified-marketing-dashboard`
- **Branch:** `main`
- **Main File:** `app.py`

## 🔑 **Environment Variables (Secrets)**
Add these in Streamlit Cloud → Settings → Secrets:

```bash
# Google Ads API
GOOGLE_ADS_DEVELOPER_TOKEN=your_developer_token_here
GOOGLE_ADS_CLIENT_ID=your_client_id_here
GOOGLE_ADS_CLIENT_SECRET=your_client_secret_here
GOOGLE_ADS_REFRESH_TOKEN=your_refresh_token_here
GOOGLE_ADS_LOGIN_CUSTOMER_ID=5426234549
GOOGLE_ADS_CUSTOMER_ID=8335511794

# Google Analytics
GOOGLE_ANALYTICS_PROPERTY_ID=your_property_id_here

# AI Chatbot (Gemini)
GOOGLE_API_KEY=your_gemini_api_key_here

# Sierra Interactive CRM
SIERRA_API_KEY=your_sierra_api_key_here
SIERRA_BASE_URL=your_sierra_base_url_here
```

## 🚀 **Deployment Steps**

### **1. Create GitHub Repository**
```bash
# Create new repository on GitHub
# Repository name: unified-marketing-dashboard
# Owner: ELevine-RE
# Description: Unified marketing dashboard for Levine Real Estate
```

### **2. Push to GitHub**
```bash
# Add remote origin
git remote add origin https://github.com/ELevine-RE/unified-marketing-dashboard.git

# Push to GitHub
git push -u origin main
```

### **3. Deploy on Streamlit Cloud**
1. Go to https://share.streamlit.io/
2. Click "New app"
3. Repository: `ELevine-RE/unified-marketing-dashboard`
4. Branch: `main`
5. Main file path: `app.py`
6. Add the secrets above
7. Click "Deploy"

## 🌐 **Final URL**
Your app will be available at:
**https://share.streamlit.io/ELevine-RE/unified-marketing-dashboard/main/app.py**

## 📁 **Clean Repository Structure**
```
unified-marketing-dashboard/
├── app.py                          # 🎯 MAIN APPLICATION
├── requirements.txt                # Dependencies
├── README.md                       # Documentation
├── DEPLOYMENT_CONFIG.md           # This file
├── .streamlit/
│   └── config.toml               # Streamlit configuration
├── .gitignore                     # Git ignore rules
├── chatbot_view.py                # AI chatbot component
├── command_center_view.py         # Command center view
├── marketing_plan_view.py         # Marketing planning
├── strategic_plan_view.py         # Strategic planning
├── google_ads_integration.py      # Google Ads API
├── google_analytics_simple.py     # Google Analytics
└── sierra_integration.py          # Sierra CRM integration
```

## ✅ **Ready to Deploy!**
This is a clean, dedicated repository with all your marketing tools consolidated into one application.
