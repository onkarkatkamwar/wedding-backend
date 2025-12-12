# Wedding Backend

A scalable multi-tenant FastAPI platform for wedding service companies. Each company operates in an isolated database environment while sharing the same application infrastructure.

## Overview

This backend provides a complete solution for wedding service providers to manage their operations independently. The multi-tenant architecture ensures data isolation while maintaining efficient resource utilization.

**Key Features:**
- Secure JWT-based authentication
- Isolated tenant databases per company
- RESTful API with automatic documentation
- Async database operations for optimal performance
- Production-ready with comprehensive validation

## Tech Stack

- **FastAPI** - Modern Python web framework
- **MongoDB** with Motor - Async NoSQL database
- **Pydantic** - Data validation
- **Passlib + bcrypt** - Secure password hashing
- **python-jose** - JWT token management

## Quick Start

### Prerequisites

- Python 3.8+
- MongoDB (local or cloud instance)
- Git

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd wedding-backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

Interactive documentation: `http://localhost:8000/docs`

## Configuration

Create a `.env` file in the root directory:

```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=wedding_master_db
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Security Note:** Always use a strong, randomly generated `SECRET_KEY` in production.

## Project Structure

```
wedding-backend/
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (not in git)
├── .env.example              # Environment template
└── app/
    ├── config.py             # Application configuration
    ├── database.py           # Database connections and tenant logic
    ├── security.py           # Authentication utilities
    ├── models.py             # Data models and schemas
    └── routes/
        ├── auth.py           # Authentication endpoints
        └── company.py        # Company management endpoints
```

## API Documentation

### Authentication

**POST** `/auth/login`
- Authenticate and receive JWT token
- Body: `{ "email": "string", "password": "string" }`
- Returns: `{ "access_token": "string", "token_type": "bearer" }`

### Company Management

**POST** `/companies/register`
- Register a new company
- Creates isolated tenant database
- Body: Company details including credentials

**GET** `/companies/{company_id}`
- Retrieve company information
- Requires authentication

**PUT** `/companies/{company_id}`
- Update company details
- Requires authentication

**DELETE** `/companies/{company_id}`
- Remove company and all associated data
- Requires authentication

## Multi-Tenant Architecture

The platform uses a database-per-tenant approach:

- **Master Collection:** `companies` - Stores company metadata and credentials
- **Tenant Collections:** `tenant_{company_name}` - Isolated data storage per company

This architecture ensures complete data separation while maintaining a single application codebase.

## Development

### Running Tests

```bash
pytest
```

### Code Quality

```bash
# Format code
black app/

# Lint
pylint app/

# Type checking
mypy app/
```

### Development with Docker

```bash
docker-compose up
```

## Deployment

This application is ready for deployment on:

- **Render** - Zero-config deployments
- **Railway** - Git-based deployments
- **AWS** - EC2, Lambda, or ECS
- **Google Cloud Run** - Serverless containers
- **Azure App Service** - Platform as a service
- **DigitalOcean App Platform** - Managed hosting

### Production Checklist

- [ ] Set strong `SECRET_KEY`
- [ ] Use production MongoDB instance
- [ ] Enable HTTPS
- [ ] Configure CORS properly
- [ ] Set up monitoring and logging
- [ ] Implement rate limiting
- [ ] Regular backups
- [ ] Security headers configured

## Roadmap

Potential enhancements:

- Role-based access control (RBAC)
- Event and booking management
- Customer portal
- Admin dashboard
- Email notifications
- Payment integration
- Analytics and reporting
- File upload support
- Real-time updates with WebSockets

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues:
- Open an issue in the GitHub repository
- Contact: [your-email@example.com]

---

Built with FastAPI and MongoDB
