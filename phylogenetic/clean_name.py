def clean_name(name: str):  
    # Remove special characters and truncate to 10 characters 
    name_ = name.replace(".", "_")
    name_ = name_.replace("variant", "v")
    pod = 0
    while (name_[pod]!='('): pod += 1

    start = 0
    while (("istone_" in name_[0:start])==False): start+=1

    
    return name_[start:pod-1]