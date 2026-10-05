package com.krushisevakendra.service;

import com.krushisevakendra.entity.BackupLog;

import java.util.List;

public interface BackupService {
    BackupLog triggerDatabaseBackup();
    List<BackupLog> getBackupHistory();
    byte[] getBackupData(String fileName);
}
