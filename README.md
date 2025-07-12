# Real Estate Agency Website

This project is a Django-based website for a real estate agency. The site is currently under development, with only the flat listing page and admin panel available for database management.

## Features

- Browse property listings with detailed information
- Filter properties by town, price range, and building type (new buildings)
- Admin panel for managing properties, owners, and complaints
- Phone number normalization for property owners
- Tracking of user favorites (liked properties)

## Prerequisites

- Python 3.9+
- Django 5.2

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/real-estate-agency.git
   cd real-estate-agency
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**  
   Create a `.env` file in the project root with the following variables:
   ```
   DEBUG=True
   SECRET_KEY=your_secret_key
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE=sqlite:///db.sqlite3
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## Environment Variables

The project uses the following environment variables:

- `DEBUG` — Debug mode. Set to True for development debugging information.
- `SECRET_KEY` — Django's secret key for security purposes.
- `ALLOWED_HOSTS` — Comma-separated list of hosts allowed to serve the application. See [Django documentation](https://docs.djangoproject.com/en/5.2/ref/settings/#allowed-hosts).
- `DATABASE` — Database URL in a single line, for example: `sqlite:///db.sqlite3`. This allows easy switching between database backends. More information in the [dj-database-url documentation](https://github.com/jacobian/dj-database-url).

## Data Models

### Flat
Represents a property listing with details such as:
- Address and location information
- Price and specifications (rooms, area)
- Construction year and building type (new/old)
- Owner information

### Owner
Stores information about property owners:
- Name
- Phone number (both raw and normalized format)
- Relationships to owned properties

### Complaint
Tracks user complaints about properties:
- User who submitted the complaint
- The property being complained about
- Complaint text and timestamp

## Project Structure

- `property/` - Main application containing models, views, and templates
- `property/models.py` - Data models for Flat, Owner, and Complaint
- `property/views.py` - View functions for rendering pages
- `property/admin.py` - Admin panel configuration
- `property/templates/` - HTML templates
- `property/migrations/` - Database migrations

## Usage

Access the web interface at http://localhost:8000/ after starting the server.

Access the admin panel at http://localhost:8000/admin/ (requires creating a superuser).

## License

This project is open-source and available under the MIT License.

## Purpose

This code was written for educational purposes as part of a Python and web development course at [Devman](https://dvmn.org).
