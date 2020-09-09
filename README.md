# Rental Price Evaluation

Project members: JJtheNOOB & [archer99076](https://github.com/archer99076)

__Goal__: To estimate apartment price based on information we can get from the website

- Step one - Pull data from the website
    - Target variable: price
    - Property type (1 bedroom, 2 bedroom etc)
    - Property geographic information (location, address etc..)
    - Property detailed information (Unit amenaties, building amenaties etc..)
    
- Step two -  Data Cleaning (modify data into the format that can be better analyzed)
   - removed duplicated columns
   - removed and merged redundant and similar columns, such as schools and school
   - modified some column type such as price column as float number
   - added some new columns such as number of dens etc
 
 - Step three - Data Modeling (Including some attempts of feature engineering)
   - Tried feature engineering (such as bed / bath ratio and single price)
   - Final accuracy IQR range +- 120 CAD
 
 - HTML Version: https://rental-model.herokuapp.com/
 - Streamlit Version: https://rental-model-jj.herokuapp.com/
   
   - Future Improvements:
    - Distributed Database (NoSQL)
    - Automate the update process
    - Adding more features on the deployment page

