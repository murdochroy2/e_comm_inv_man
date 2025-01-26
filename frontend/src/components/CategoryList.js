import React, { useState, useEffect } from 'react';
import styles from './CategoryForm.module.css';
import { categoryService } from '../services/api';

const CategoryList = ({ categories, onDeleteCategory }) => {
    const [selectedCategory, setSelectedCategory] = useState(null);
    const [products, setProducts] = useState([]);

    const handleCategoryChange = (event) => {
        const categoryId = Number(event.target.value);
        const category = categories.find(cat => cat.id === categoryId);
        setSelectedCategory(category);
    };

    useEffect(() => {
        if (selectedCategory) {
            const fetchProducts = async () => {
                const data = await categoryService.getCategoryDetails(selectedCategory.id);
                setProducts(data.products);
                
                setSelectedCategory(prev => ({ ...prev, ...data }));
            };
            fetchProducts();
        }
    }, [selectedCategory]);

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
            {products.length > 0 && (
                <div className={styles.productList}>
                    <h4>Products:</h4>
                    <table>
                        <thead>
                            <tr>
                                <th>Product Name</th>
                                <th>SKU</th>
                            </tr>
                        </thead>
                        <tbody>
                            {products.map(product => (
                                <tr key={product.id}>
                                    <td>{product.name}</td>
                                    <td>{product.sku}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
};

export default CategoryList; 