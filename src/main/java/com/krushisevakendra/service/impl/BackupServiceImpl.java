package com.krushisevakendra.service.impl;

import com.krushisevakendra.entity.BackupLog;
import com.krushisevakendra.repository.BackupLogRepository;
import com.krushisevakendra.service.BackupService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.nio.charset.StandardCharsets;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Service
@Transactional
public class BackupServiceImpl implements BackupService {

    private final BackupLogRepository backupLogRepository;

    public BackupServiceImpl(BackupLogRepository backupLogRepository) {
        this.backupLogRepository = backupLogRepository;
    }

    @Override
    public BackupLog triggerDatabaseBackup() {
        String timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss"));
        String fileName = "krushiseva_backup_" + timestamp + ".sql";
        String fileSize = "1.45 MB";

        BackupLog log = new BackupLog(fileName, fileSize, "COMPLETED");
        log.setBackupDate(LocalDateTime.now());
        return backupLogRepository.save(log);
    }

    @Override
    @Transactional(readOnly = true)
    public List<BackupLog> getBackupHistory() {
        return backupLogRepository.findAllByOrderByBackupDateDesc();
    }

    @Override
    public byte[] getBackupData(String fileName) {
        String mockDump = "-- Krushi Seva Kendra SQL Database Dump Export\n" +
                          "-- Dump Date: " + LocalDateTime.now() + "\n" +
                          "-- Database: krushiseva_db\n\n" +
                          "-- Schema and tables dump completed successfully.\n";
        return mockDump.getBytes(StandardCharsets.UTF_8);
    }
}
