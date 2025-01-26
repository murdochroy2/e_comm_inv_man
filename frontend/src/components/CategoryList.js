import React, { useState } from 'react';
import styles from './CategoryForm.module.css';

const CategoryList = ({ categories, onDeleteCategory }) => {
    const [selectedCategory, setSelectedCategory] = useState(null);

    const handleCategoryChange = (event) => {
        const categoryId = Number(event.target.value);
        const category = categories.find(cat => cat.id === categoryId);
        setSelectedCategory(category);
    };

    return (
        <div className={styles.formContainer}>
            <h2>Categories</h2>
            <select onChange={handleCategoryChange} value={selectedCategory ? selectedCategory.id : ''}>
                <option value="">Select a category</option>
                {categories.map((category) => (
                    <option key={category.id} value={category.id}>
                        {category.name}
                    </option>
                ))}
            </select>
            {selectedCategory && (
                <div className={styles.categoryDetails}>
                    <h3>{selectedCategory.name}</h3>
                    <p>{selectedCategory.description}</p>
                </div>
            )}
        </div>
    );
};

export default CategoryList; 