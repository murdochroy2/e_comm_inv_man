import React, { useState, useEffect } from 'react';
import CategoryForm from './CategoryForm';
import CategoryList from './CategoryList';
import ProductManagement from './ProductManagement';
import { categoryService } from '../services/api';
import styles from './CategoryForm.module.css';

const InventoryManagement = () => {
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        loadCategories();
    }, []);

    const loadCategories = async () => {
        try {
            const data = await categoryService.getAllCategories();
            setCategories(data);
        } catch (error) {
            console.error('Error loading categories:', error);
        }
    };

    const handleCategoryAdded = (newCategory) => {
        setCategories([...categories, newCategory]);
    };

    const handleDeleteCategory = async (categoryId) => {
        try {
            await categoryService.deleteCategory(categoryId);
            setCategories(categories.filter(cat => cat.id !== categoryId));
        } catch (error) {
            alert('Error deleting category');
        }
    };

    return (
        <div className="inventory-management">
            <h1>Inventory Management System</h1>
            
            <div className={styles.managementSection}>
                <div className={styles.categorySection}>
                    <h2>Category Management</h2>
                    <CategoryForm onCategoryAdded={handleCategoryAdded} />
                    <CategoryList 
                        categories={categories} 
                        onDeleteCategory={handleDeleteCategory}
                    />
                </div>
                
                <div className={styles.productSection}>
                    <h2>Product Management</h2>
                    <ProductManagement categories={categories} />
                </div>
            </div>
        </div>
    );
};

export default InventoryManagement; 