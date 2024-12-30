# My React Wallet Connection App

## Overview
This project is a React application that allows users to connect their cryptocurrency wallets, register their wallet addresses, and claim daily points. The application is built using the following technologies:

- **React** for the frontend.
- **RainbowKit** for wallet connection.
- **Flask** for the backend API.
- **SQLite** as the database.

## Features
1. **Wallet Connection**: Users can connect their wallets using the RainbowKit library.
2. **Wallet Registration**: Automatically registers connected wallets in the database.
3. **Daily Points Claim**: Users can claim points daily (once every 24 hours).
4. **View Points**: Displays the total points accumulated by the user.
5. **API Integration**: Seamlessly communicates with the backend API to register wallets and manage points.

## Installation

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/my-react-wallet-app.git
   cd my-react-wallet-app/backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

## Usage
1. Open the frontend in your browser (default: `http://localhost:3000`).
2. Connect your wallet using the "Connect Wallet" button.
3. Click "Claim Daily Points" to earn points (once per day).
4. View your total points on the interface.

## API Endpoints

### 1. **Register Wallet**
   - **Endpoint**: `/register`
   - **Method**: `POST`
   - **Payload**:
     ```json
     {
       "wallet_address": "<wallet_address>"
     }
     ```
   - **Response**:
     ```json
     {
       "status": "success",
       "message": "Wallet registered successfully."
     }
     ```

### 2. **Claim Points**
   - **Endpoint**: `/claim_points`
   - **Method**: `POST`
   - **Payload**:
     ```json
     {
       "wallet_address": "<wallet_address>"
     }
     ```
   - **Response**:
     ```json
     {
       "status": "success",
       "points": 10
     }
     ```

## Deployment

### Deploying Frontend
1. Use a platform like **Vercel** or **Netlify**.
2. Link your GitHub repository.
3. Deploy the `frontend` folder as the root directory.

### Deploying Backend
1. Use a platform like **Heroku** or **Render**.
2. Configure your Python environment and database setup.
3. Deploy the `backend` folder as the root directory.

## Future Enhancements
1. **Custom Wallet Integration**: Add support for more wallets.
2. **Leaderboard**: Display a leaderboard of users with the highest points.
3. **Notifications**: Notify users when they can claim points again.

## Contributing
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

