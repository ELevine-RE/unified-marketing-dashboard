# 🏡 Levine Real Estate - Unified Marketing Dashboard

A consolidated Streamlit application that combines all your marketing tools into a single accessible web interface.

## 🌐 **Deploy to Streamlit Cloud**
**Repository:** `ELevine-RE/unified-marketing-dashboard`  
**Main File:** `app.py`  
**Branch:** `main`

## 🎯 **What's Included**

This unified dashboard consolidates all your separate repositories and tools:

### 📊 **Main Analytics Dashboard**
- Google Ads campaign performance
- Google Analytics website metrics  
- Sierra Interactive CRM data
- Real-time performance monitoring
- Interactive charts and visualizations

### 🤖 **AI Campaign Manager**
- Powered by Google Gemini AI
- Natural language campaign management
- Function calling for Google Ads operations
- Campaign performance analysis
- Budget and campaign control

### 📅 **Marketing Plan & Timeline**
- Seasonal marketing initiatives
- Weekly task tracking with checkboxes
- Timeline visualization
- Goal setting and progress monitoring
- Strategic framework reference

### 📋 **Strategic Planning Framework**
- Three-pillar marketing philosophy
- Demand Generation, Capture, and Nurturing
- Strategy calendar and project planning
- Production timeline templates

### 🎮 **Command Center**
- Unified view of all data sources
- Advanced analytics and insights
- Performance optimization recommendations
- Cross-platform data correlation

### 🔧 **System Diagnostics**
- Integration status monitoring
- API connection health checks
- Environment configuration status
- Troubleshooting information

## 🚀 **Quick Start**

### **Option 1: Streamlit Cloud (Recommended)**
1. Push this repository to GitHub
2. Connect to Streamlit Cloud
3. Set environment variables for API keys
4. Deploy automatically

### **Option 2: Local Development**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 🔑 **Environment Variables**

Set these in your Streamlit Cloud secrets or local environment:

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
GOOGLE_ANALYTICS_CREDENTIALS_PATH=path_to_credentials.json

# AI Chatbot
GOOGLE_API_KEY=your_gemini_api_key

# Sierra Interactive CRM
SIERRA_API_KEY=your_sierra_api_key
SIERRA_BASE_URL=your_sierra_url
```

## 📁 **Repository Consolidation**

This unified tool combines components from:

- ✅ `google-ads-analysis` - Main dashboard and analytics
- ✅ `ELevine-RE/google-ads-analysis` - GitHub repository
- ✅ `marketing-plan-timeline` - Marketing planning tools
- ✅ `ELevine-RE/marketing-plan-timeline` - GitHub repository  
- ✅ `levine-real-estate-website/chatbot_view.py` - AI chatbot

**All accessible from one URL instead of multiple repositories!**

## 🛠️ **Features**

### **Smart Fallbacks**
- Uses mock data when APIs are unavailable
- Graceful degradation for missing integrations
- Clear status indicators for each component

### **Responsive Design**
- Wide layout optimized for dashboards
- Sidebar navigation for easy switching
- Mobile-friendly interface

### **Real-time Updates**
- Live data refresh capabilities
- Session state management
- Interactive charts and metrics

## 📊 **Data Sources**

- **Google Ads API** - Campaign performance, costs, conversions
- **Google Analytics** - Website traffic, user behavior, goals
- **Sierra Interactive** - CRM leads, contact management
- **Google Gemini AI** - Natural language processing for chatbot

## 🔧 **Technical Stack**

- **Frontend:** Streamlit
- **Charts:** Plotly
- **Data:** Pandas, NumPy
- **AI:** Google Gemini
- **APIs:** Google Ads, Google Analytics, Sierra Interactive
- **Deployment:** Streamlit Cloud

## 📈 **Usage**

1. **Navigate** using the sidebar to switch between tools
2. **Monitor** performance on the main dashboard
3. **Chat** with the AI assistant for campaign management
4. **Plan** marketing initiatives using the timeline
5. **Track** progress with strategic planning tools
6. **Analyze** data in the command center
7. **Diagnose** issues using system diagnostics

## 🆘 **Support**

- Check the **Diagnostics** page for system status
- Review environment variable configuration
- Test API connections individually
- Use mock data for development/testing

## 📝 **Notes**

- All components are now consolidated into a single application
- No need to manage multiple repositories
- Single URL access for all tools
- Consistent user experience across all features
- Easy deployment and maintenance

---

**🎯 Mission:** Provide a unified, accessible platform for all Levine Real Estate marketing operations through a single, powerful web application.
