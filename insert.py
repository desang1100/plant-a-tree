import openpyxl

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Select the active sheet
sheet = workbook.active

# Define the dataset
dataset = [
            [1, "Area Size", "Project Scope", "Soil Condition", "weather condition", "participant",'Time'],
            
            [2, "small", "urban planting", "fair", "rainy", "_small",'C'],
            [3, "small", "agroforestry", "poor", "cloudy", "very_small","B"],
            [4, "medium", "agroforestry", "good", "sunny", "_medium","A"],
            [5, "medium", "urban planting", "fair", "rainy", "_small",'B'],
            [6, "medium", "reforestation", "good", "cloudy", "_small",'A'],
            [7, "very small", "agroforestry", "poor", "sunny", "very_small","B"],
            [8, "small", "agroforestry", "fair", "rainy", "_small","D"],
            [9, "large", "reforestation", "good", "cloudy", "_medium","B"],
            [10, "very large", "urban planting", "fair", "sunny", "very_large","E"],
            [11, "large", "reforestation", "poor", "sunny", "_large", "C"],
            [12, "medium", "urban planting", "good", "rainy", "_medium", "B"],
            [13, "small", "agroforestry", "fair", "cloudy", "_small", "A"],
            [14, "very small", "urban planting", "good", "sunny", "very_small", "D"],
            [15, "very large", "reforestation", "fair", "rainy", "_large", "E"],
            [16, "large", "agroforestry", "poor", "cloudy", "_large", "A"],
            [17, "small", "reforestation", "good", "sunny", "_small", "B"],
            [18, "medium", "urban planting", "fair", "rainy", "_medium", "C"],
            [19, "very large", "agroforestry", "good", "cloudy", "_large", "D"],
            [20, "very small", "reforestation", "fair", "sunny", "very_small", "E"],
            [21, "small", "reforestation", "good", "sunny", "_small", "A"],
            [22, "large", "urban planting", "fair", "rainy", "_large", "B"],
            [23, "medium", "agroforestry", "poor", "cloudy", "_medium", "C"],
            [24, "very large", "agroforestry", "good", "sunny", "_large", "D"],
            [25, "very small", "urban planting", "fair", "rainy", "very_small", "E"],
            [26, "large", "reforestation", "good", "cloudy", "_large", "A"],
            [27, "small", "agroforestry", "poor", "sunny", "_small", "B"],
            [28, "medium", "agroforestry", "good", "rainy", "_medium", "C"],
            [29, "very small", "urban planting", "fair", "cloudy", "very_small", "D"],
            [30, "large", "reforestation", "good", "sunny", "_large", "E"],
            [31, "small", "agroforestry", "poor", "rainy", "_small", "A"],
            [32, "medium", "urban planting", "good", "cloudy", "_medium", "B"],
            [33, "very large", "agroforestry", "fair", "sunny", "_large", "C"],
            [34, "very small", "reforestation", "good", "rainy", "very_small", "D"],
            [35, "large", "urban planting", "fair", "cloudy", "_large", "E"],
            [36, "medium", "agroforestry", "poor", "sunny", "_medium", "A"],
            [37, "small", "reforestation", "good", "rainy", "_small", "B"],
            [38, "large", "urban planting", "fair", "sunny", "_large", "C"],
            [39, "medium", "agroforestry", "good", "cloudy", "_medium", "D"],
            [40, "very small", "reforestation", "fair", "rainy", "very_small", "E"],
            [41, "small", "agroforestry", "good", "cloudy", "_small", "A"],
            [42, "large", "urban planting", "fair", "sunny", "_large", "B"],
            [43, "medium", "reforestation", "poor", "rainy", "_medium", "C"],
            [44, "very large", "agroforestry", "good", "cloudy", "_large", "D"],
            [45, "very small", "urban planting", "fair", "sunny", "very_small", "E"],
            [46, "large", "agroforestry", "poor", "cloudy", "_large", "A"],
            [47, "small", "reforestation", "good", "sunny", "_small", "B"],
            [48, "medium", "urban planting", "fair", "rainy", "_medium", "C"],
            [49, "very large", "agroforestry", "good", "cloudy", "_large", "D"],
            [50, "very small", "reforestation", "fair", "sunny", "very_small", "E"],
         
            
        ]

# Insert the dataset into the Excel file
for row in dataset:
    sheet.append(row)

# Save the workbook
workbook.save("dataset.xlsx")
