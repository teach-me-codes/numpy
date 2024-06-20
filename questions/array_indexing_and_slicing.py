questions = [
    {
        'Main question': 'What is array indexing in NumPy and how does it work?',
        'Explanation': 'The candidate should explain the concept of array indexing in NumPy, involving accessing individual elements or subsets by specifying indices or slices.',
        'Follow-up questions': ['Demonstrate the syntax for indexing a specific element in a NumPy array.', 'How can array indexing access multiple elements at once in a NumPy array?', 'Advantages of using array indexing over traditional iteration for element access?']
    },
    {
        'Main question': 'What is array slicing in NumPy and why is it useful?',
        'Explanation': 'The candidate should describe array slicing in NumPy, allowing extraction of subsets based on start, stop, and step parameters.',
        'Follow-up questions': ['Applying array slicing to extract specific rows or columns from a multidimensional NumPy array.', 'Differences between shallow copy and deep copy in array slicing.', 'Scenarios where array slicing is more efficient than array indexing for data manipulation.']
    },
    {
        'Main question': 'How can negative indexing be used in NumPy arrays?',
        'Explanation': 'The candidate should explain negative indexing in NumPy, accessing elements from the end of an array for relative referencing.',
        'Follow-up questions': ['Outcome when a negative index exceeds array length in NumPy?', 'Example of using negative indexing to access elements from the end of a NumPy array.', 'Simplification of operations using negative indexing compared to positive indexing in NumPy?']
    },
    {
        'Main question': 'What are the different ways to slice a one-dimensional NumPy array?',
        'Explanation': 'The candidate should discuss methods for slicing a 1D NumPy array, including basic and advanced slicing, and using boolean masks for filtering based on conditions.',
        'Follow-up questions': ['Differences between basic and advanced slicing in syntax and functionality.', 'Significance of broadcasting when working with sliced NumPy arrays.', 'Utilizing boolean masking for extracting elements meeting specific criteria from a NumPy array.']
    },
    {
        'Main question': 'How does array slicing in NumPy differ between one-dimensional and multidimensional arrays?',
        'Explanation': 'The candidate should compare slicing techniques for 1D and multidimensional arrays in NumPy, emphasizing indexing differences across multiple axes.',
        'Follow-up questions': ['Challenges associated with slicing multidimensional arrays in NumPy.', 'Using ellipsis (...) for accessing specific elements in multidimensional arrays.', 'Impact of broadcasting on slicing operations for multidimensional NumPy arrays.']
    },
    {
        'Main question': 'What is the difference between view and copy in NumPy array slicing?',
        'Explanation': 'The candidate should explain the distinction between a view and a copy when slicing NumPy arrays and how modification affects data and memory.',
        'Follow-up questions': ['Determining whether a slice is a view or a copy.', 'Risks of inadvertently modifying original data with views in NumPy array slicing.', 'Examples where creating views or copies of array slices is preferred for memory efficiency and data integrity.']
    },
    {
        'Main question': 'How can step values in NumPy array slicing skip elements during extraction?',
        'Explanation': 'The candidate should demonstrate using step values to skip elements in array slicing, improving efficiency for tasks like downsampling or decimation.',
        'Follow-up questions': ['Outcome when a negative step value is used in array slicing.', 'Beneficial scenarios for specifying step values in slicing large NumPy arrays.', 'Impact of step value choice on size and content of extracted sliced arrays from larger arrays in NumPy.']
    },
    {
        'Main question': 'Can you explain how NumPy handles out-of-bounds indices during array slicing?',
        'Explanation': 'The candidate should clarify NumPy\'s behavior with out-of-bounds indices in array slicing operations, addressing exceeds array dimensions or negative indices beyond array length.',
        'Follow-up questions': ['Error messages or exceptions when encountering out-of-bounds indices in NumPy array slicing.', 'Optimizing boundary checks for array indices to enhance slicing performance in NumPy.', 'Handling out-of-bounds indices impact on data integrity and correctness during array slicing in NumPy.']
    },
    {
        'Main question': 'How does NumPy handle assignment during array slicing for modifying array elements?',
        'Explanation': 'The candidate should describe in-place modification of array elements using array slicing and assignment operations in NumPy.',
        'Follow-up questions': ['Considerations when assigning values to sliced subsets for data consistency.', 'Differences between direct and reference assignment when modifying elements via array slicing in NumPy.', 'Benefits of utilizing NumPy\'s broadcasting within assignment operations for array slicing tasks.']
    },
    {
        'Main question': 'How can Boolean indexing be utilized in NumPy for advanced data selection?',
        'Explanation': 'The candidate should demonstrate Boolean masks for filtering elements based on conditional expressions, allowing versatile data extraction beyond traditional slicing in NumPy.',
        'Follow-up questions': ['Advantages of using Boolean indexing over traditional slicing for element extraction in NumPy.', 'Applying complex filtering conditions with multiple Boolean masks efficiently in large NumPy arrays.', 'Enhancing readability and maintainability of code with Boolean indexing during data selection tasks in NumPy.']
    }
]