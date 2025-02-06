# Receipt Processor API

## Tech Stack
- **Language**: Java
- **Framework**: Spring Boot
- **Containerization**: Docker

---

## Installation and Running the Application

### **Steps : Run with Docker**
1. **Clone the Repository**
   ```sh
   https://github.com/jiemazhb/Backend-Take-Home-Exercise-Fetch.git
2. **Build the Docker Image**
   ```sh
   docker build -t receipt-processor .
4. **Run the Docker Container**
   ```sh
   docker run -p 8080:8080 receipt-processor
6. **Use Postman to make API calls**
   - Post Request: URL and Request Body:
  <br><br>
   ```sh
     http://localhost:8080/receipts/process


     {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
      {
        "shortDescription": "Mountain Dew 12PK",
        "price": "6.49"
      },{
        "shortDescription": "Emils Cheese Pizza",
        "price": "12.25"
      },{
        "shortDescription": "Knorr Creamy Chicken",
        "price": "1.26"
      },{
        "shortDescription": "Doritos Nacho Cheese",
        "price": "3.35"
      },{
        "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
        "price": "12.00"
      }
    ],
    "total": "35.35"
    }
     ```
   
   - Get Requet : 
    ```sh
     http://localhost:8080/receipts/{id}/points
