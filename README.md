# Quran Hadith Verse Finder

### **Context:** <br/>

In Islam, it is recommended for every Muslim to live life based on the Quran and Hadith. The Quran, also romanized as Qur'an or Koran, is the central religious text of Islam, believed by Muslims to be a direct revelation from God (Allah). The Hadith is a source of religious and moral guidance known as Sunnah, ranking second in authority only to the Quran.

People who can memorize every verse of the Quran are known as Hafiz. However, it is not feasible for every Muslim to memorize all the verses related to a particular topic. While search engines like Google can help address this issue, they often provide too many links and websites, making it difficult to find authentic information. It would be more efficient to have a tool that provides related verses in one place with just one click.

### **Objective:**

The goal of this project is to build an application that retrieves Quran and Hadith verses based on user queries with just one click. This project includes data collection from authentic sources, data cleaning, embedding, deployment, and API integration.

### **Data Collection:**

This project includes data collection from authentic sources that are 
1. [quran.com](https://quran.com/)
2. [sunnah.com](https://sunnah.com/)

Only Four Hadith books were scraped that are *Sahih al-Bukhari*, *Sahih Muslim*, *Sunan an-Nasa'i* and *Sunan Abi Dawud*. Scraping codes/scripts can be found in `scraper` folder.

### **Data Preparation :** <br/>

The data was thoroughly checked before creating the vector database. Each verse was concatenated with its corresponding surah or hadith so that the retrieval can include the name of the surah or hadith book. The cleaned data can be found in the `data` folder. The data preparation process is documented in `notebooks/Quran_Hadith_Semantic_Search.ipynb`.

### **Vector Database creation:**

The model used to embed the dataset is `sentence-transformers/all-MiniLM-L6-v2`. Model documentation can be found [here](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). This model is specialized for creating semantic sarch application with its sentence embedding capability. The embeddings/ vector database can be found in `model/ embeddings.pkl`.

### **HuggingFace Deployment:**

The model along with the entire pipeline has been deployed in huggingface spaces using gradio interface. You can visit the spcae via [this link](https://huggingface.co/spaces/mhdhrubo/quran_hadith_verse_finder).

### **Web Deployment using API integration:**

Deployed a Flask App built to take user input/query and show the similar verses related to the query. Check the flask  branch or [click here](https://github.com/moinul-hossain-dhrubo/quran_hadith_verse_finder/tree/flask). Live website can be found [here](https://quran-hadith-verse-finder.onrender.com/).

![quran_hadith_app_home](https://github.com/user-attachments/assets/27bf614c-e15b-4d94-b7b4-d3141cb19a71)

![quran_hadith_app_result](https://github.com/user-attachments/assets/1c7466d3-dcf1-4199-86b0-4f037831eb48)


