import joblib

def main():
    # Load the model from the file path
    model = joblib.load('/d:/ML Projects/Phishing Detection Model/phishmodel.pkl')

    # Get the URL from the user
    url = input("Enter the URL to check: ")

    # Use the model to predict if the URL is phishing or not
    prediction = model.predict([features])

    # Print the prediction
    if prediction[0] == 1:
        print("The URL is phishing.")
    else:
        print("The URL is not phishing.")

if __name__ == '__main__':
    main()
