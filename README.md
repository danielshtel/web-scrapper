# Web-scrapper

## _Service for [tesmanian.com](https://www.tesmanian.com/)_

Scrapping the latest articles from [tesmanian.com](https://www.tesmanian.com/blogs/tesmanian-blog) and auto-publishing
posts
to [Tesmanian](https://t.me/tesmanian) telegram channel.

## Tech:

- Python 3.10
- requests
- Beautifulsoup4
- PostgreSQL
- Telebot
- Docker

## Installation

### Clone the project

```shell
git clone git@github.com:danielshtel/web-scrapper.git
```

⚠️ **Copy env.tmpl to `.env` and substitute the default values with your own usernames and passwords.**

### Web-scrapper Docker:

**Make sure you set environment variables in `.env`**

```shell
cd web-scrapper
```

#### To run services (with logs):

```shell
docker-compose up
```

#### To stop services:

```shell
docker-compose down
```

#### If you want to remove all your data, use:

```shell
docker volume prune
```

### How it works? 🤔

Welcome to my demo telegram channel [Tesmanian](https://t.me/tesmanian) to see how it works! 🎇\
**Subscribe** and read actual news! 

