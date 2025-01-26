import React, { useState } from 'react';
import { categoryService } from '../services/api';
import styles from './CategoryForm.module.css';

const CategoryForm = ({ onCategoryAdded }) => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const newCategory = await categoryService.createCategory({ name, description });
            onCategoryAdded(newCategory);
            setName('');
            setDescription('');
        } catch (error) {
            alert('Error creating category');
        }
    };

    return (
        <div className={styles.formContainer}>
            <h2>Add New Category</h2>
            <form onSubmit={handleSubmit}>
                <div className={styles.formGroup}>
                    <label htmlFor="name">Category Name:</label>
                    <input
                        type="text"
                        id="name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    />
                </div>
                <div className={styles.formGroup}>
                    <label htmlFor="description">Description:</label>
                    <textarea
                        id="description"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                    />
                </div>
                <button type="submit">Add Category</button>
            </form>
        </div>
    );
};

export default CategoryForm; 