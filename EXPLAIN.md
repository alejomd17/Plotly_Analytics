# Sales Analysis Dashboard with Plotly/Dash

## Architecture Overview

The project follows a modular, layered architecture:

      sales-analysis-dash/
      ├── app.py
      ├── src/
      │   ├── __init__.py
      │   ├── app_instance.py
      │   ├── callbacks.py
      │   ├── get_data.py
      │   └── layouts.py
      ├── assets/
      │   ├── styles.css
      │   └── fonts/
      ├── data/
      │   ├── dataset.csv
      ├── EXPLAIN.md
      ├── README.md
      └── requirements

## App Design

1. **Data preprocessing**:
   - All preprocessing was developed in `src/get_data.py`,
   - First at all, I create the function `load_and_preprocess_data()` where I convert the object columns that could be converted in **datetime**. I extracted the **year, month and quearter** as separated columns, and I created the combine columns `year_quarter` and `year_month`, to facilitate the temporal analysis.
   - **Note: Data filtering**
   For this exercise is important to comment that I eliminated all the 2022 information because it hadn't enough information (Actually I created a loop which is looking for the quantity of registers in a year, and if that amount is less than 1000 then I won't work with this year).

2. **Metrics calculation**:
   - The function `calculate_yoy_growth()` is used to calculate the **percentage difference** between the month or quarter againts the same period of the last year. Also, this function create some **supporting columns** for the visualization.
   - **Total sales** are a simple aggregation by `year_month` and `year_quarter`.

3. **Interactivity**:
   - The function `get_data(segments, categories, time_resolution)` is receiving the parameters `segments, categories, time_resolution` that are used for the interactivity of the app.
   - The `segments and categories` are filtering the dataframe and the `time_resolution` is used to calculate the growth and sales metrics explained in the last point.
   - Finally, I have two dataframes to plot: **Sales and growth graphs**, which are filtered according to the **segments, categories and time_resolution**

4. **App Instance**:
   - I create a module in the module `src/app_instance.py`, that provides as a **centralized configuration** of the app.
   - It is allowing a unified inicialization: it create a **unique instance of the Dash** app that will be consumed by the rest of the moduls.
   - Also, it centralizes the initial configuration (asset) and ensures that the entire application uses the same **Dash instance**.

5. **Callbacks and plots**:
   - The callback that update the plots was developed in the module `src/callbacks.py`,
   - First, it is calling the app: `@app.callback` to update the **inputs** and outputs. For this exercise the inputs are `segment, category and time`, these are used to create the dataframes that are used to plot the graph.
   The **outputs** are the graph and growth graphs.
   - According to the above, in the function `update_charts` the graphs are created using plotly, both being are **barplot** because the quantity of data is small.
   - Both are improved using plotly function `.update_layout` for the title, background and grid and .`.update_traces` for show the numbers in numeric format
   
4. **Layouts**:
   - The layouts are developed in the module `src/layouts.py`,
   - Also, it is using a styles in css (Into the assets folder `assets/styles.css`) to make more beautiful the app.
   - In the same folder (assets) there is another folder with some fonts that I think are similar to the ones used in the YipitData Home Assignment file.
   - For the layouts I create, 3 different Divisions:
      1. A title: `app-title`
      2. A `filter-container`: Which includes another 2 divisions:
         * In the first row **dropdown-row**: I create a Div `dropdown-container` where I implement **filters for segments and categories** using **dropdowns multi-select**
         * In the second row **radio-row**: I create a Div `radio-container` where I added a **selector** in order to change the view between quarter and month.
      This will allow the charts to update automatically when changing filters.
      3. A `graphs-container`: Where the Dash graphs (ddc) are located (It means, the outputs that the callbacks return us)

5. **Initialization & Assembly**
   - `app.py` file serves as the **entry point** and orchestration hub for the Dash application.
   - Coordinates the union of all modules:
      - Takes the preconfigured Dash instance (`app_instance.py`)
      - Imports the visual framework (`layouts.py`)
      - Registers the interactive logic (`callbacks.py`)

## Observed Insights
   - There are not **enough data for considering using 2022**, so It was deleted of the analysis.
   - The graph show a seasonal patterns in the Q3 and the month 09 september.
   - Looks like something happened in the 202103 and forward, because it was showing a good behaviour but inmediatly it starts to decrease. This may have been Covid.
   - The Year-on-year growth shows a reduction in the sales around 6%-10% aprox.
   - It doesn't exist an specific period of "prime", in 2020 was Q2 and 2021 was Q1, but it is normal that in the month 11 have an amazing register.

## Decisions of the design

1. **Prioritize Functionality over Style**:
   - According the instructions, I focus on clarity and correctness rather than styling
   - The interface is minimalist but functional

2. **Code organization**:
   - I separed the steps: the preprocessing of the data, the layouts and the callbacks, in order to have clean code and OOP.
   - Also I create an app_instance to centralized the configuration of the app.