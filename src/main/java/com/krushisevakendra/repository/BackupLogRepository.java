package com.krushisevakendra.repository;

import com.krushisevakendra.entity.BackupLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface BackupLogRepository extends JpaRepository<BackupLog, Long> {
    List<BackupLog> findAllByOrderByBackupDateDesc();
}
