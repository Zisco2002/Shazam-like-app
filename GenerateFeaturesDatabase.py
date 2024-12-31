import shutil
import json
from pathlib import Path
import ComputeHashedFeatures

# Save the hashed features locally
def saveHash(wavFile, featuresHash, outputDirectory):
    # Prepares the data to be saved in a JSON file
    result = {
        "featuresHash": featuresHash
    }

    # Creates the output directory
    outputDirectory.mkdir(parents=True, exist_ok=True)

    # Creates the output file path
    outputFile = outputDirectory / wavFile.with_suffix(".json").name # .name extract the file name part without the path (after it was changed from .wav to .json)

    with open(outputFile, "w") as f:
        json.dump(result, f, indent=4) # The indent=4 argument makes the JSON output pretty printed 
    
# Loop over our dataset and save the computed hashed features for each song file
inputDirectory = Path("./task5_data")
outputDirectory = Path("./task5_hashes")
if outputDirectory.exists():
        shutil.rmtree(outputDirectory)

for file in inputDirectory.glob("*.wav"):
    hashedFeatures = ComputeHashedFeatures.processHash(file)
    saveHash(file, hashedFeatures, outputDirectory)