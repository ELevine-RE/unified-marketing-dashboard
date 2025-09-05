# 🚀 Deployment Guide - Unified Marketing Dashboard

## 🌐 **Target URL**
**https://levine-real-estate-website-4nxq5aaspozpfyed5gsxsk.streamlit.app/**

## 📋 **Deployment Steps**

### **Step 1: Prepare Repository**
```bash
# Navigate to your WebTool directory
cd /Users/evan/WebTool

# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Consolidated marketing dashboard - all tools in one app"

# Add remote repository
git remote add origin https://github.com/ELevine-RE/levine-real-estate-website.git

# Push to GitHub
git push -u origin main
```

### **Step 2: Streamlit Cloud Deployment**

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with your GitHub account

2. **Create New App**
   - Click "New app"
   - Repository: `ELevine-RE/levine-real-estate-website`
   - Branch: `main`
   - Main file path: `app.py`

3. **Configure Environment Variables**
   In the Streamlit Cloud dashboard, add these secrets:

   ```bash
   # Google Ads API
   GOOGLE_ADS_DEVELOPER_TOKEN=your_token
   GOOGLE_ADS_CLIENT_ID=your_client_id
   GOOGLE_ADS_CLIENT_SECRET=your_client_secret
   GOOGLE_ADS_REFRESH_TOKEN=your_refresh_token
   GOOGLE_ADS_LOGIN_CUSTOMER_ID=5426234549
   GOOGLE_ADS_CUSTOMER_ID=8335511794

   # Google Analytics
   GOOGLE_ANALYTICS_PROPERTY_ID=your_property_id

   # AI Chatbot
   GOOGLE_API_KEY=your_gemini_api_key

   # Sierra Interactive CRM
   SIERRA_API_KEY=your_sierra_api_key
   SIERRA_BASE_URL=your_sierra_url
   ```

4. **Deploy**
   - Click "Deploy"
   - Wait for build to complete
   - Your dashboard will be live!

## 🔧 **Local Testing**

### **Option 1: Direct Run**
```bash
cd /Users/evan/WebTool
streamlit run app.py
```

### **Option 2: With Environment Variables**
```bash
# Set environment variables
export GOOGLE_API_KEY="your_gemini_api_key"
export GOOGLE_ADS_DEVELOPER_TOKEN="your_token"
# ... other variables

# Run the app
streamlit run app.py
```

## 📁 **File Structure**

```
/Users/evan/WebTool/
├── app.py                          # Main unified application
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
├── DEPLOYMENT_GUIDE.md            # This file
├── .streamlit/
│   └── config.toml               # Streamlit configuration
├── chatbot_view.py                # AI chatbot component
├── command_center_view.py         # Command center view
├── marketing_plan_view.py         # Marketing planning
├── strategic_plan_view.py          # Strategic planning
├── google_ads_integration.py      # Google Ads API
├── google_analytics_simple.py     # Google Analytics
└── sierra_integration.py          # Sierra CRM integration
```

## 🎯 **What This Consolidates**

### **Before (Multiple Repositories):**
- ❌ `google-ads-analysis` - Separate dashboard
- ❌ `ELevine-RE/google-ads-analysis` - GitHub repo
- ❌ `marketing-plan-timeline` - Separate timeline tool
- ❌ `ELevine-RE/marketing-plan-timeline` - GitHub repo
- ❌ `levine-real-estate-website/chatbot_view.py` - Separate chatbot

### **After (Single Application):**
- ✅ **One URL:** https://levine-real-estate-website-4nxq5aaspozpfyed5gsxsk.streamlit.app/
- ✅ **All Tools:** Dashboard, Chatbot, Planning, Analytics
- ✅ **Unified Experience:** Consistent navigation and design
- ✅ **Easy Maintenance:** Single codebase to manage

## 🔍 **Testing Checklist**

- [ ] App loads without errors
- [ ] All navigation tabs work
- [ ] Mock data displays correctly
- [ ] Chatbot interface renders (even without API key)
- [ ] Marketing plan timeline displays
- [ ] Strategic plan framework shows
- [ ] Command center loads
- [ ] Diagnostics page shows system status

## 🚨 **Troubleshooting**

### **Build Fails**
- Check `requirements.txt` has all dependencies
- Verify Python version compatibility
- Check for syntax errors in `app.py`

### **No Data Showing**
- Verify environment variables are set correctly
- Check API credentials and permissions
- Review integration status in Diagnostics page

### **Chatbot Not Working**
- Ensure `GOOGLE_API_KEY` is set
- Check Gemini API quota and billing
- Verify API key has proper permissions

## 📞 **Support**

If you encounter issues:
1. Check the **Diagnostics** page in the app
2. Review environment variable configuration
3. Test API connections individually
4. Use mock data for development/testing

---

**🎉 Success!** You now have all your marketing tools consolidated into a single, accessible web application at one URL!
