import pandas as pd

df = pd.read_excel("egitim.xlsx", "Sheet1")
Age = df['Age'].values.tolist()
Gender = df['Gender'].values.tolist()
Air_Pollution = df['Air Pollution'].values.tolist()
Alcohol_Use = df['Alcohol use'].values.tolist()
Dust_Allergy = df['Dust Allergy'].values.tolist()
OccuPational_Hazards = df['OccuPational Hazards'].values.tolist()
Genetic_Risk = df['Genetic Risk'].values.tolist()
chronic_Lung_Disease = df['chronic Lung Disease'].values.tolist()
Balanced_Diet = df['Balanced Diet'].values.tolist()
Obesity = df['Obesity'].values.tolist()
Smoking = df['Smoking'].values.tolist()
Passive_Smoker = df['Passive Smoker'].values.tolist()
Chest_Pain = df['Chest Pain'].values.tolist()
Coughing_of_Blood = df['Coughing of Blood'].values.tolist()
Fatigue = df['Fatigue'].values.tolist()
Weight_Loss = df['Weight Loss'].values.tolist()
Shortness_of_Breath = df['Shortness of Breath'].values.tolist()
Wheezing = df['Wheezing'].values.tolist()
Swallowing_Difficulty = df['Swallowing Difficulty'].values.tolist()
Clubbing_of_Finger_Nails = df['Clubbing of Finger Nails'].values.tolist()
Frequent_Cold = df['Frequent Cold'].values.tolist()
Dry_Cough = df['Dry Cough'].values.tolist()
Snoring = df['Snoring'].values.tolist()
Level = df['Level'].values.tolist()
Levels = []

for i in range(0, len(Level)):

    if (Level[i] == 'Low'):
        Levels.append([0,0])
    elif (Level[i] == 'Medium'):
        Levels.append([0,1])
    elif (Level[i] == 'High'):
        Levels.append([1,1])

def Norm(x, min, max):
    xYeni = (x - min) / (max-min)
    return xYeni

for i in range(0, len(Age)):
    Age[i] = Norm(Age[i], min(Age), max(Age))
    Gender[i] = Norm(Gender[i], min(Gender), max(Gender))
    Air_Pollution[i] = Norm(Air_Pollution[i], min(Air_Pollution), max(Air_Pollution))
    Alcohol_Use[i] = Norm(Alcohol_Use[i], min(Alcohol_Use), max(Alcohol_Use))
    Dust_Allergy[i] = Norm(Dust_Allergy[i], min(Dust_Allergy), max(Dust_Allergy))
    OccuPational_Hazards[i] = Norm(OccuPational_Hazards[i], min(OccuPational_Hazards), max(OccuPational_Hazards))
    Genetic_Risk[i] = Norm(Genetic_Risk[i], min(Genetic_Risk), max(Genetic_Risk))
    chronic_Lung_Disease[i] = Norm(chronic_Lung_Disease[i], min(chronic_Lung_Disease), max(chronic_Lung_Disease))
    Balanced_Diet[i] = Norm(Balanced_Diet[i], min(Balanced_Diet), max(Balanced_Diet))
    Obesity[i] = Norm(Obesity[i], min(Obesity), max(Obesity))
    Smoking[i] = Norm(Smoking[i], min(Smoking), max(Smoking))
    Passive_Smoker[i] = Norm(Passive_Smoker[i], min(Passive_Smoker), max(Passive_Smoker))
    Chest_Pain[i] = Norm(Chest_Pain[i], min(Chest_Pain), max(Chest_Pain))
    Coughing_of_Blood[i] = Norm(Coughing_of_Blood[i], min(Coughing_of_Blood), max(Coughing_of_Blood))
    Fatigue[i] = Norm(Fatigue[i], min(Fatigue), max(Fatigue))
    Weight_Loss[i] = Norm(Weight_Loss[i], min(Weight_Loss), max(Weight_Loss))
    Shortness_of_Breath[i] = Norm(Shortness_of_Breath[i], min(Shortness_of_Breath), max(Shortness_of_Breath))
    Wheezing[i] = Norm(Wheezing[i], min(Wheezing), max(Wheezing))
    Swallowing_Difficulty[i] = Norm(Swallowing_Difficulty[i], min(Swallowing_Difficulty),
                                    max(Swallowing_Difficulty))
    Clubbing_of_Finger_Nails[i] = Norm(Clubbing_of_Finger_Nails[i], min(Clubbing_of_Finger_Nails),
                                       max(Clubbing_of_Finger_Nails))
    Frequent_Cold[i] = Norm(Frequent_Cold[i], min(Frequent_Cold), max(Frequent_Cold))
    Dry_Cough[i] = Norm(Dry_Cough[i], min(Dry_Cough), max(Dry_Cough))
    Snoring[i] = Norm(Snoring[i], min(Snoring), max(Snoring))

cols = 700
rows = 23
Pgiris = [[0 for i in range(cols)] for j in range(rows)]
for j in range(0, 700):
    Pgiris[0][j] = Age[j]
    Pgiris[1][j] = Gender[j]
    Pgiris[2][j] = Air_Pollution[j]
    Pgiris[3][j] = Alcohol_Use[j]
    Pgiris[4][j] = Dust_Allergy[j]
    Pgiris[5][j] = OccuPational_Hazards[j]
    Pgiris[6][j] = Genetic_Risk[j]
    Pgiris[7][j] = chronic_Lung_Disease[j]
    Pgiris[8][j] = Balanced_Diet[j]
    Pgiris[9][j] = Obesity[j]
    Pgiris[10][j] = Smoking[j]
    Pgiris[11][j] = Passive_Smoker[j]
    Pgiris[12][j] = Chest_Pain[j]
    Pgiris[13][j] = Coughing_of_Blood[j]
    Pgiris[14][j] = Fatigue[j]
    Pgiris[15][j] = Weight_Loss[j]
    Pgiris[16][j] = Shortness_of_Breath[j]
    Pgiris[17][j] = Wheezing[j]
    Pgiris[18][j] = Swallowing_Difficulty[j]
    Pgiris[19][j] = Clubbing_of_Finger_Nails[j]
    Pgiris[20][j] = Frequent_Cold[j]
    Pgiris[21][j] = Dry_Cough[j]
    Pgiris[22][j] = Snoring[j]
