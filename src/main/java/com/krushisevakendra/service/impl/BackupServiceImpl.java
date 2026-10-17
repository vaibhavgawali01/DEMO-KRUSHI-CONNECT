package com.krushisevakendra.service.impl;

import com.krushisevakendra.entity.BackupLog;
import com.krushisevakendra.repository.BackupLogRepository;
import com.krushisevakendra.service.BackupService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

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
        throw new UnsupportedOperationException(
                "Database backup is unavailable: no database dump provider is configured. No backup was created.");
    }

    @Override
    @Transactional(readOnly = true)
    public List<BackupLog> getBackupHistory() {
        return backupLogRepository.findAllByOrderByBackupDateDesc();
    }

    @Override
    public byte[] getBackupData(String fileName) {
        throw new UnsupportedOperationException("No database backup file is available for download.");
    }
}
