# **Gemini Explorer**  
**An interactive AI-powered chat interface using Google's Vertex AI and Streamlit.** 🚀

## **Description**  
Gemini Explorer is a **chatbot** powered by **Google's Gemini AI** models, allowing users to have interactive conversations through a web-based interface built with **Streamlit**. This project leverages **Google Cloud Vertex AI** to generate dynamic responses, adapting to user input and style.

## **Features**  
✨ **Gemini Explorer** offers the following features:  
- **Chat directly** with **Gemini AI** in your browser.  
- Stores **conversation history** for contextual and engaging responses.  
- **Adapts** to user style and maintains interactive conversation.  
- A simple, **web-based interface** built using **Streamlit**.

## **Installation & Setup**  

### **1️⃣ Create a Virtual Environment**  
Before running the project, create and activate a virtual environment:  

#### **Windows**  
```sh
python -m venv env
env\Scripts\activate
```  
#### **MacOS/Linux**  
```sh
python3 -m venv env
source env/bin/activate
```
---

### **2️⃣ Install Dependencies**  
Once the virtual environment is activated, install the required packages:  
```sh
pip install -r requirements.txt
```

Your **requirements.txt** should include:  
```
streamlit
google-cloud-aiplatform
vertexai
python-dotenv
```
---

### **3️⃣ Set up a Google Cloud Project**  

#### **Step 1: Create Google Cloud Account**  
1. Go to [Google Cloud Platform](https://cloud.google.com/) and sign up for a new account or log in if you already have one.
2. **Account Verification:**
    - Google provides free credits, but you’ll need to verify your account by entering billing information. Rest assured, you won't be charged at this stage.  

#### **Step 2: Set Up Billing**  
1. Ensure your **billing information** is accurate and up-to-date.
2. Make use of the **free trial** and credits for new users. After credits are exhausted or the trial ends, you'll need to upgrade to a paid plan.

#### **Step 3: Create a Project for Gemini Explorer**  
1. In the Google Cloud console, create a new project named **Gemini Explorer**.
2. Navigate to **Vertex AI** and enable the required APIs for your project.

---

### **4️⃣ Setup Google SDK**  

#### **Step 1: Download Google Cloud SDK**  
1. Visit the [Google Cloud SDK webpage](https://cloud.google.com/sdk) and download the installer for your OS.
2. Follow the installation instructions.

#### **Step 2: Initialize Google Cloud SDK**  
Once installed, initialize the SDK:  
```sh
gcloud init
```
Follow the instructions to log in to your Google Cloud account and configure your default project.

#### **Step 3: Set Up Default Project & Configuration**  
Ensure that your **Google Cloud project** is correctly initialized by running:  
```sh
gcloud init
```

If authentication issues arise, authenticate with:  
```sh
gcloud auth application-default login
```
---

### **5️⃣ Authenticate with Google Cloud**  
Ensure that **Google Cloud SDK** is installed and authenticated:  
```sh
gcloud auth application-default login
```

Also, set your **Google Cloud project**:  
```sh
gcloud init
```

⚠️ **Important:** Ensure that the **Vertex AI API** is enabled in the Google Cloud Console.

---

### **6️⃣ Set Up the Project in Code**  
Replace the **Project ID** in `gemini_explorer.py` with your **Google Cloud Project ID**:  
```python
project = "your-google-cloud-project-id"
vertexai.init(project=project)
```

## **Running the Chatbot**  

Once setup is complete, run the chatbot with:  
```sh
streamlit run gemini_explorer.py
```
This will launch a **web-based chat interface** to interact with the AI model. 💬


## **How It Works**  

1️⃣ **Streamlit** app initializes **Vertex AI's generative model** (`gemini-2.0-flash-exp`).  
2️⃣ **Chat history** is stored in **session state**, ensuring continuity.  
3️⃣ The AI begins by asking for the user's name and adapting to their conversation style.  
4️⃣ **User inputs** are processed in real-time, with responses displayed dynamically.  
5️⃣ The AI **remembers past interactions**, making the conversation more contextual.  


## **Future Enhancements**  
🔹 Add **user authentication** for personalized chats.  
🔹 Improve the **UI** with additional **Streamlit** components.  
🔹 Integrate with **external APIs** for extended functionality.


## **Contributors**  
👤 **Juily Deshpande** - *Developer & Maintainer*
```