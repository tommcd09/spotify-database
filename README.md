# Designing and Cleaning a Spotify Database in SQLite

## Overview

This project designs and cleans a database of Spotify songs, artists, and genres using SQLite. The data comes from a Kaggle data set containing about 600k tracks and 1 million artists from Spotify from 1921 to 2020. While this is by no means close to all the music on Spotify, it is enough to include a lot of great music from a wide range of time periods.

## Data

The data comes from [this Kaggle data set](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks?select=tracks.csv), which is licensed under the [Community Data License Agreement – Sharing, Version 1.0](https://cdla.dev/sharing-1-0/). The data consists of two .csv files, one for tracks and one for artists. However, in the completed database, the data is normalized into five tables according to the following schema:

![Final DB Schema](images/diagram2.png)
