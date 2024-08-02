# Quran_Hadith_verse_finder

### **Context:** <br/>

In Islam, It is recommended to live life based on Quran and Hadith for every muslims. The Quran, also romanized Qur'an or Koran, is the central religious text of Islam, believed by Muslims to be a revelation directly from God (Allah). The authority of hadith is a source for religious and moral guidance known as Sunnah, which ranks second only to that of the Quran (which Muslims hold to be the word of God revealed to Muhammad).

The people who can memorize every Quran verses is known as Ha'fiz. However, it is not possible for every muslim to memorize every verse related to a certain topic. Search engines like Google can help resolving this issue but sometimes there are too many places/ websites to click on to find the authentic information. it will be better if one can find related verses in one place with just one click.

### **Objective:**

The goal of this project is to build an application that can retrieve Quran and Hadith verses based on user query just with one click. This project includes data collection from authentic sources, data cleaning, embedding, deployment, API integration.

### **Data Collection:**

This project includes data collection from authentic sources that are 
1. [quran.com](https://quran.com/)
2. [sunnah.com](https://sunnah.com/)

Only Four Hadith books were scraped that are Sahih al-Bukhari, Sahih Muslim, Sunan an-Nasa'i and Sunan Abi Dawud. Scraping codes/scripts can be found in `scraper` folder.

### **Data Preparation :** <br/>

The data was checked thoroughly before creating the vector database. Each verse was concatenated with its corresponding surah/ hadith so that while retrieving it can also come up with the name of the surah or hadith book. The cleaned data can be found in `data` folder.

### **Vector Database creation:**

The model that was used to embed the dataset is `sentence-transformers/all-MiniLM-L6-v2`. Model documentation can be found [here](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). This model is specialized for creating semantic sarch application with its sentence embedding capability. The embeddings/ vector database can be found in `model/ embeddings.pkl`.

### **HuggingFace Deployment:**

The model along with the entire pipeline has been deployed in huggingface spaces using gradio interface. You can visit the spcae via [this link](https://huggingface.co/spaces/mhdhrubo/quran_hadith_verse_finder).

### **Web Deployment using API integration:**

Deployed a Flask App built to take user input/query and show the similar verses related to the query. Check the flask  branch or [click here](https://github.com/moinul-hossain-dhrubo/quran_hadith_verse_finder/tree/flask). Live website can be found [here](https://quran-hadith-verse-finder.onrender.com/).
