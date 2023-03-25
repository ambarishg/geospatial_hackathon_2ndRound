The **Geographical Text Analysis Question Answering System**  takes a Question , extracts the geographical locations [ Cities , States , Places ] and provides the Latitude and Longitude of the locations. This can be an effective way of getting geographical information from unstructured data.      

The application uses the following:
1. **Azure Open AI** to answer the question asked by the user       
2. We use **spacy** , an industrial strength Natural Language processing library to extract the `geographical` locations from the text         
3. We use the library **geopy** to convert the geographical locations into `latitudes` and `longitudes`          

