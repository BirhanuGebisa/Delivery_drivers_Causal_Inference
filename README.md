# Causal Inference

## Logistic optimization: Delivery drivers location optimization with Causal Inference

> Initial system architecture design

![](screen_shots/doagriam-diagram.png)

## Project details

**Table of contents**

- [Causal Inference](#causal-inference)
  - [Logistic optimization: Delivery drivers location optimization with Causal Inference](#logistic-optimization-delivery-drivers-location-optimization-with-causal-inference)
  - [Project details](#project-details)
  - [Introduction](#introduction)
  - [Overview](#overview)
  - [Objective](#objective)
  - [Data](#data)
  - [Requirements](#requirements)
  - [Install](#install)
  - [Screenshots](#screenshots)
  - [Notebooks](#notebooks)
  - [Approaches](#approaches)
  - [Models](#models)
  - [Tests](#tests)
  - [Author](#author)

## Introduction

> Data is everywhere. In order to get the best out of it, one needs to extract it from several sources, make required transformations and 

## Overview

> A startup called Mela (our client for this week’s project) wants to make it simple for everyone to enter the world of cryptocurrencies and general stock market trade. It also wants to give investors a reliable source of investment while lowering the risk associated with trading cryptocurrencies.



## Objective

> This objective of this project is very straightforward: design and build a robust, reliable, large-scale 

## Data

There are two datasets available for this project.


The first one is the table that contains information about the completed orders
>   Column             Non-Null Count   Dtype 
---  ------            --------------   ----- 
 > 0   Trip ID           536020 non-null  int64 
 > 1   Trip Origin       536020 non-null  address
 > 2   Trip Destination  536020 non-null  address
 > 3   Trip Start Time   534369 non-null  timestamp
 > 4   Trip End Time     536019 non-null  timestamp
 
The second one is the table that contains delivery requests by clients (completed and unfulfilled) 
>   Column         Non-Null Count    Dtype  
---  ------         --------------    -----  
> 0   id                1557740 non-null  int64  
> 1   order_id          1557740 non-null  int64  
> 2   driver_id         1557740 non-null  int64  
> 3   driver_action     1557740 non-null  object 
> 4   lat               1557740 non-null  float64
> 5   lng               1557740 non-null  float64
> 6   created_at        0 non-null        float64
> 7   updated_at        0 non-null        float64

## Requirements

> Pip

> Python 3.5 or above

> Docker and Docker compose

You can find the full list of requirements in the requirements.txt file

## Install

> We highly recommend you create a new virtual environment and install every required modules and libraries on the virtual environment.

## Screenshots

> The detailed use and implementation of the pipelines using Apache Airflow, pipeline summary and interaction, kafka clusters, interaction with the topics on the kafka clusters, front-end images and usage can all be found in this screenshots folder as image files.

## Notebooks

> All the notebooks that are used in this project including EDA, data cleaning and summarization along with some machine learning model generations are found here in the Notebooks folder.

## Approaches

> All the scripts and modules used for this project relating to interactions with kafka, airflow, and other frameworks along with default parameters and values used will be found here, in the scripts folder.

## Models

> All the back testing strategies and algorithms are found here in the strategies folder.

## Tests

> All the unit and integration tests are found here in the tests folder.

## Author

> 👤 **Birhanu Gebisa**
>
> - [Email](mailto:birhanugebisa@gmail.com), [GitHub](https://github.com/BirhanuGebisa), [LinkedIn](https://www.linkedin.com/in/birhanu-gebisa2721/)

> Show us your support

> Give us a ⭐ if you like this project, and also feel free to contact us at any moment.
