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

> This week's challenge task interim report focuses on causal inference using real-world Nigeria
Gokada delivery driver service data. Gokada is one of the largest last-mile delivery services in
Nigeria.

## Overview

> Current business challenges center on the causal inference of our client Gokada, Nigeria's largest
last-mile delivery service. Gokada Works is partnered with motorbike owners and drivers to
deliver parcels across Lagos, Nigeria. Gokada has completed more than a million deliveries in
less than a year with a fleet of over 1200 riders. One key issue Gokada has faced as it expands its
service is the suboptimal placement of pilots (Gokada calls their motor drivers pilots) and clients
who want to use Gokada to send their parcels. As a result, a large number of delivery requests
have gone unfulfilled.



## Objective

> This objective of this project is very straightforward: design and build a robust, reliable, large-scale It is working on its data to help it understand the primary causes of
unfulfilled requests, as well as come up with solutions that recommend driver locations that
increase the fraction of complete orders. Since drivers are paid based on the number of requests
they accept, this solution will help Gokada business grow both in terms of client satisfaction and
increased business volume.

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

> The detailed use and implementation of the pipelines drivers location optimization with Causal Inference
usage can all be found in this screenshots folder as image files.

## Notebooks

> All the notebooks that are used in this project including EDA, data cleaning and summarization along with some machine learning model generations are found here in the Notebooks folder.

## Approaches

> All the scripts and modules used for this project relating to interactions drivers location optimization with Causal Inference
 and other frameworks along with default parameters and values used will be found here, in the scripts folder.

## Models

> All the drivers location optimization with Causal Inference are found here in the strategies folder.

## Tests

> All the unit and integration tests are found here in the tests folder.

## Author

> 👤 **Birhanu Gebisa**
>
> - [Email](mailto:birhanugebisa@gmail.com), [GitHub](https://github.com/BirhanuGebisa), [LinkedIn](https://www.linkedin.com/in/birhanu-gebisa2721/)

> Show us your support

> Give us a ⭐ if you like this project, and also feel free to contact us at any moment.
