package com.intermedisoft.imedx.dao;

import java.util.List;

/**
 * Generic DAO interface - Legacy Java 8 style
 * @param <T> Entity type
 * @param <ID> Primary key type
 */
public interface GenericDao<T, ID> {
  /**
   * Save or update entity
   * @param entity Entity to save
   * @return Saved entity with generated ID
   */
  T save(T entity);

  /**
   * Find entity by ID
   * @param id Primary key
   * @return Entity or null if not found
   */
  T findById(ID id);

  /**
   * Find all entities
   * @return List of all entities
   */
  List<T> findAll();

  /**
   * Update existing entity
   * @param entity Entity to update
   * @return Updated entity
   */
  T update(T entity);

  /**
   * Delete entity by ID
   * @param id Primary key
   * @return true if deleted, false otherwise
   */
  boolean deleteById(ID id);

  /**
   * Delete entity
   * @param entity Entity to delete
   * @return true if deleted, false otherwise
   */
  boolean delete(T entity);

  /**
   * Check if entity exists by ID
   * @param id Primary key
   * @return true if exists, false otherwise
   */
  boolean existsById(ID id);

  /**
   * Count total entities
   * @return Total count
   */
  long count();
}
