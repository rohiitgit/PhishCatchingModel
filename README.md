***Project Documentation: Phishing URL Detection***

**Introduction**
In an era where digital threats continue to grow in complexity and frequency, the need for robust solutions to combat cybercriminal activities has become paramount. Phishing attacks, characterized by their deceptive mimicry of legitimate websites, stand as one of the most prevalent and dangerous tactics employed by cybercriminals to compromise users worldwide. These attacks often involve the distribution of malicious links or websites through various mediums such as email, SMS, and social messaging, with the primary aim of duping unsuspecting users into divulging sensitive information or downloading malicious payloads.

To counter this pervasive threat, our project endeavors to harness the power of Artificial Intelligence (AI) and Machine Learning (ML) to create an intelligent system that can effectively detect phishing domains. These domains typically masquerade as genuine websites, making their identification a formidable challenge.

Our system is designed to scrutinize newly registered domains, leveraging open-source databases like the WHOIS database, which provides a list of these recently registered websites. It employs a range of innovative techniques to distinguish phishing domains from legitimate ones:

Backend Code and Content Similarity Analysis: Our system analyzes the underlying code and content of web pages to identify discrepancies and similarities with known genuine websites. The greater the likeness to a known phishing attempt, the higher the probability score.

Web Page Image Analysis: A unique aspect of our system involves the comparison of web page images between known genuine websites and potentially malicious ones. The more similar a phishing site's web page images are to the genuine counterparts, the stronger the likelihood of it being a lookalike phishing site.

The efficacy of our system is evaluated based on its ability to:

- Assign probability scores to phishing domains, indicating their proximity to genuine domains.
- Detect new phishing domains in a timely and efficient manner.
- Offer ease of use and flexibility in output formats, making it accessible and adaptable to a range of user needs.

In a landscape where cyber threats evolve rapidly, our project aims to provide a sophisticated yet user-friendly tool that   can bolster online security by proactively identifying and mitigating phishing attacks. This documentation serves as a comprehensive guide to the system's functionality, usage, and potential for future development, making it a valuable resource for both cybersecurity professionals and novices alike.

**Features**
1. Phishing Domain Identification: The system aims to differentiate phishing domains from legitimate ones, particularly among newly registered websites. It leverages open-source databases like the WHOIS database, which provide data on recently registered domains.

2. Sophisticated Techniques: The system uses cutting-edge AI and ML techniques, including backend code/content similarity analysis and web page image analysis. These methods are crucial for assessing the likelihood of a domain being a phishing site.

3. Probability Scoring: Phishing domains are assigned probability scores based on how closely they resemble genuine domains. Higher scores indicate a greater likelihood of being a phishing site.

4. Rapid Detection: The system is designed to swiftly identify new phishing domains, ensuring that potential threats are spotted in real time.

5. User-Friendly Interface: It offers ease of use and flexibility in output formats, making it accessible and adaptable to a wide range of users, including cybersecurity professionals and beginners.


**System Architecture**
The architecture of the AI/ML-based Phishing Domain Detection System is designed to efficiently and accurately identify phishing domains among newly registered websites. The system comprises several key components that work collaboratively to achieve this goal. Below is an overview of the system's architecture:

1. Data Sources:

    WHOIS Database: The system relies on the WHOIS database, which provides information about newly registered domains. This data source is essential for identifying potential phishing domains.

2. Data Collection and Processing:

    Data Retrieval: The system periodically collects data from the WHOIS database, focusing on newly registered domains.
    Data Preprocessing: It preprocesses the retrieved data, extracting relevant information, such as domain registration details and timestamps.

3. Machine Learning Models:

    Model Training: The system employs AI/ML models that have been trained on a large dataset of known phishing and genuine domains. These models serve as the foundation for phishing detection.
    Feature Extraction: Feature extraction techniques are used to prepare data for model input, including backend code attributes and web page image data.

4. Phishing Detection Techniques:

    Backend Code and Content Analysis: This component performs a detailed analysis of the backend code and content of web pages associated with the domains. It assesses similarities and discrepancies between these elements and known genuine websites.
    Web Page Image Analysis: This component compares web page images of potentially malicious domains with images from genuine websites. Image analysis plays a crucial role in determining the likelihood of a domain being a lookalike phishing site.

5. Probability Scoring:

    The system assigns probability scores to each domain based on the results of the detection techniques. Higher scores indicate a greater likelihood of a domain being a phishing site.

6. Detection and Alerting:

    Domains with high probability scores are flagged as potential phishing sites. The system provides alerts for further investigation.

7. User Interface:

    The system offers a user-friendly interface that allows users to input domains for analysis and view the results. It provides flexibility in output formats, ensuring that users can access information in their preferred way.


8. Integration Options:

    The system can be integrated with other security tools or platforms to provide a comprehensive security solution.

**High-level architectural diagram**


**Prerequisites**

- Python
- Tensorflow
- Keras
- BeautifulSoup
- Requests
- urllib
- re
- tldextract
- spacy


**Getting Started**

Installation instructions:
In terminal, run:
pip install requirements.txt


**Machine Learning Models**

The heart of our AI/ML-based Phishing Domain Detection System lies in the ensemble of sophisticated machine learning models. These models are meticulously crafted to analyze domain data, detect patterns, and distinguish phishing domains from genuine ones. The ensemble consists of the following five machine learning models:

*TensorFlow and Keras Neural Network*
Description: The TensorFlow and Keras Neural Network is a deep learning model capable of handling complex, high-dimensional data. It excels in identifying intricate patterns within domain-related features.

Training Data: This model has been trained on a diverse dataset containing a wide range of features, including backend code attributes and web page content.

Strengths:

- Capability to uncover subtle patterns and irregularities in domain data.
- Excellent performance in handling unstructured data, such as web page content and images.
- Adaptability to evolving phishing tactics due to its deep architecture.

*Support Vector Classifier (SVC)*
Description: The Support Vector Classifier is a powerful classification model that effectively separates domains into distinct categories based on their characteristics.

Training Data: The SVC model is trained on a labeled dataset comprising features extracted from known phishing and genuine domains.

Strengths:

- Strong capability to create well-defined decision boundaries, making it effective at domain classification.
- Robustness in the face of outliers and noisy data.

*Logistic Regression*
Description: Logistic Regression is a simple yet effective model that excels at binary classification tasks. It is particularly valuable in the early stages of domain analysis.

Training Data: The Logistic Regression model uses labeled data to learn to distinguish between phishing and genuine domains.

Strengths:

- Quick and efficient for binary classification tasks.
- Transparency and interpretability, making it suitable for preliminary domain assessment.

*Random Forest Tree*
Description: The Random Forest Tree is an ensemble model composed of multiple decision trees. It combines their outputs to make robust predictions.

Training Data: This model is trained on a dataset containing a variety of features, including code attributes and web page data.

Strengths:

- Robust against overfitting and able to handle high-dimensional data.
- Enhanced accuracy through the aggregation of multiple decision trees.

*Gradient Boost*
Description: Gradient Boost is an ensemble model that builds a series of decision trees iteratively. It focuses on improving prediction accuracy with each new tree added.

Training Data: The Gradient Boost model uses labeled data for training, making it increasingly accurate over time.

Strengths:

- Ability to improve model accuracy through iterative learning.
- Effective in capturing complex relationships within the data.

**Training data and model training process**

Numerical Features:

1. *NumDots*: The number of dots in the URL.
2. *SubdomainLevel*: The level of subdomains in the URL.
3. *PathLevel*: The level of paths in the URL.
4. *UrlLength*: The length of the URL.
5. *NumDash*: The number of dashes in the URL.
6. *NumDashInHostname*: The number of dashes in the hostname.
7. *AtSymbol*: Presence of the "@" symbol in the URL.
8. *TildeSymbol*: Presence of the "~" symbol in the URL.
9. *NumUnderscore*: The number of underscores in the URL.
10. *NumPercent*: The number of percent signs in the URL.
11. *NumQueryComponents*: The number of query components in the URL.
12. *NumAmpersand*: The number of ampersands in the URL.
13. *NumHash*: The number of hash symbols in the URL.
14. *NumNumericChars*: The number of numeric characters in the URL.
15. *NoHttps*: Whether HTTPS is missing in the URL.
16. *RandomString*: Presence of random characters in the URL.
17. *IpAddress*: Presence of an IP address in the URL.
18. *DomainInSubdomains*: The presence of the domain in subdomains.
19. *DomainInPaths*: The presence of the domain in paths.
20. *HttpsInHostname*: Presence of HTTPS in the hostname.
21. *HostnameLength*: The length of the hostname.
22. *PathLength*: The length of the path.
23. *QueryLength*: The length of the query component.
24. *DoubleSlashInPath*: Presence of double slashes in the path.
25. *NumSensitiveWords*: The number of sensitive words in the URL.
26. *EmbeddedBrandName*: The presence of embedded brand names.

Binary Features:

27. *PctExtHyperlinks*: The percentage of external hyperlinks.
28. *PctExtResourceUrls*: The percentage of external resource URLs.
29. *ExtFavicon*: Presence of external favicons.
30. *InsecureForms*: Presence of insecure forms.
31. *RelativeFormAction*: Use of relative form actions.
32. *ExtFormAction*: Presence of external form actions.
33. *AbnormalFormAction*: Abnormal form actions.
34. *PctNullSelfRedirectHyperlinks*: Percentage of null self-redirect hyperlinks.
35. *FrequentDomainNameMismatch*: Frequent domain name mismatches.
36. *FakeLinkInStatusBar*: Presence of fake links in the status bar.
37. *RightClickDisabled*: Disabling of right-click functionality.
38. *PopUpWindow*: Presence of pop-up windows.
39. *SubmitInfoToEmail*: Submission of information to an email address.
40. *IframeOrFrame*: Presence of iframes or frames.
41. *MissingTitle*: Missing webpage title.
42. *ImagesOnlyInForm*: Images-only forms.

Ternary Features:

43. *SubdomainLevelRT*: Subdomain level relative to the domain.
44. *UrlLengthRT*: URL length relative to the domain.
45. *PctExtResourceUrlsRT*: Percentage of external resource URLs relative to the domain.
46. *AbnormalExtFormActionR*: Abnormal external form actions relative to the domain.
47. *ExtMetaScriptLinkRT*: Percentage of external meta, script, or link tags relative to the domain.
48. *PctExtNullSelfRedirectHyperlinksRT*: Percentage of external null self-redirect hyperlinks relative to the domain.

These features provide a rich dataset for training your machine learning models, enabling them to effectively differentiate between phishing domains and genuine ones based on various characteristics and behaviors commonly associated with phishing attempts

**9. Evaluation**
Phishing Domain Detection System's Performance Evaluation

The effectiveness of our AI/ML-based Phishing Domain Detection System is critical for its real-world application. We assess the system's performance through the following key metrics:

Probability Scores: We evaluate the accuracy of probability scores assigned to domains. Higher scores indicate a stronger likelihood of a domain being a phishing site.

Timely Detection: The system's ability to detect new phishing domains in a prompt manner is assessed, ensuring real-time threat mitigation.

Ease of Use: We prioritize user-friendliness and offer flexibility in output formats to cater to users with varying needs.

Our ongoing monitoring and continuous model updates are integral to maintaining and improving the system's performance.


***Real World Used***
1. Email Security:

    Detecting malicious links and phishing attempts in email communications to protect users from fraudulent emails.
2. Web Browsing Security:

    Identifying phishing websites in real-time as users navigate the web, helping them avoid potentially harmful sites.
3. Online Banking and Finance:

    Enhancing security in online banking by identifying phishing domains attempting to steal users' financial information.
4. E-commerce and Online Shopping:

    Protecting consumers from fake online stores that aim to steal payment information or sell counterfeit goods.
5. Social Media Safety:

    Scanning links and content shared on social media platforms to prevent the spread of phishing attacks through social channels.
6. Educational Institu tions:

    Safeguarding students and staff from phishing emails that might compromise personal and institutional data.
7. Government and Public Sector:

    Detecting and blocking phishing attacks on government websites, safeguarding sensitive information and citizen data.
8. Healthcare and Medical Data:
 
    Ensuring the security of medical data and patient information by identifying phishing threats targeting healthcare providers and patients.
9. Small and Medium-Sized Businesses:

    Providing affordable and effective phishing detection solutions for smaller enterprises that may lack extensive cybersecurity resources.
10. Web Hosting and Domain Providers:

    Incorporating your system into domain registration and hosting services to proactively prevent the registration and hosting of phishing domains.
11. Mobile Apps and App Stores:

    Ensuring the safety of mobile app users by detecting and blocking links to phishing websites.
12. IoT Security:

    Protecting Internet of Things (IoT) devices and networks by identifying and blocking potential threats through phishing domains.
13. Online Advertisements:

    Preventing the distribution of malicious advertisements and links that could lead to phishing sites.
14. Travel and Booking Services:

    Securing online booking platforms from fraudulent websites aiming to scam travelers or steal personal data.
16. Non-Profit Organizations:

    Protecting donors and supporters from phishing campaigns targeting the organization's online presence.

***Future Developments***
14. Future Developments
Advancing the Phishing Domain Detection System

Our AI/ML-based Phishing Domain Detection System is a dynamic and evolving tool that continues to adapt to the ever-changing landscape of cyber threats. To ensure its continued effectiveness and relevance, several potential avenues for future development and enhancement have been identified:

14.1. Enhanced Feature Engineering
    Incorporate additional relevant features and data sources to improve the system's ability to identify phishing domains. Continuous feature engineering can capture emerging phishing tactics.

14.2. Reinforcement Learning
    Integrate reinforcement learning to enhance the system's ability to make real-time decisions and adapt to novel threats dynamically.

14.3. User Behavior Analysis
    Incorporate user behavior analysis to identify anomalous behavior patterns that may indicate phishing attempts and improve user-level security.

14.4. Threat Intelligence Integration
    Integrate threat intelligence feeds to receive real-time updates on new phishing threats and adapt the system accordingly.

14.5. Explainability and Transparency
    Enhance model interpretability to provide detailed insights into why a domain is flagged as a potential threat. Transparency and interpretability are essential for user trust.

14.6. Cross-Platform Coverage
    Extend the system's coverage to mobile devices and applications to protect users across a broader range of platforms.

14.7. Machine Learning Model Updates
    Continuously update and fine-tune the machine learning models to adapt to new phishing tactics and improve detection accuracy.

14.8. Cloud-Based Solution
    Develop a cloud-based version of the system to enable scalability and real-time updates, making it accessible to a broader user base.

14.9. Regulatory Compliance
    Ensure the system's compliance with evolving cybersecurity regulations and standards, keeping it aligned with the latest legal requirements.

14.10. Collaboration with Industry Partners
    Collaborate with industry partners and organizations to share threat intelligence and jointly develop solutions for emerging threats.

14.11. Crowdsourced Data Collection
    Leverage crowdsourced data collection to expand the system's dataset and improve its detection capabilities.

14.12. Educational Initiatives
    Continue to educate users about the latest phishing threats and best practices to prevent falling victim to attacks.

These future developments aim to bolster the system's effectiveness, accuracy, and adaptability, ensuring it remains a robust tool for combating phishing attacks. Regular updates and enhancements will allow the system to stay ahead of evolving threats and provide users with the highest level of security in an ever-changing digital landscape.