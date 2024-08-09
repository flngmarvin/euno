from tqdm import tqdm

# Example function where verbose controls tqdm
def process_data(data, verbose=1):
    if verbose > 0:
        iterator = tqdm(data, desc="Processing data", unit="item")
    else:
        iterator = data  # No progress bar if verbose is 0 or less
        
    processed_data = []
    for item in iterator:
        # Process each item
        processed_item = process_item(item)
        processed_data.append(processed_item)
        if verbose > 0:
            iterator.set_postfix({"processed_items": len(processed_data)})
    
    return processed_data

# Example usage
data_to_process = range(1000)
processed_data = process_data(data_to_process, verbose=2)
