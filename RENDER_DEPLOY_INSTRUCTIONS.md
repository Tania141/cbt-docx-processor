# 🚀 Render.com Deploy Инструкции

## СТЪПКА 1: Създай GitHub Repository (5 мин)

### **А) Създай нов repo:**
1. Отиди на https://github.com
2. Влез с акаунта си (или създай нов)
3. Кликни **"New repository"** (зелен бутон горе вдясно)
4. Име: `cbt-docx-processor`
5. Описание: `DOCX processing API for CBT projects`
6. **Public** (задължително за Render free tier)
7. ✅ Add README file
8. Кликни **"Create repository"**

### **Б) Upload файловете:**

**Вариант 1 - Чрез уеб интерфейс (най-лесно):**
1. В новия repo кликни **"Add file"** → **"Upload files"**
2. Upload следните 3 файла:
   - `app.py`
   - `requirements.txt`
   - `.python-version`
3. Commit message: "Initial commit - DOCX processor API"
4. Кликни **"Commit changes"**

**Вариант 2 - Чрез Git (ако имаш Git):**
```bash
git clone https://github.com/[твоето-username]/cbt-docx-processor.git
cd cbt-docx-processor
# Copy файловете app.py, requirements.txt, .python-version тук
git add .
git commit -m "Initial commit - DOCX processor API"
git push
```

---

## СТЪПКА 2: Deploy на Render.com (5 мин)

### **А) Регистрация:**
1. Отиди на https://render.com
2. Кликни **"Get Started"**
3. Избери **"Sign up with GitHub"** (най-лесно)
4. Разреши достъп до GitHub

### **Б) Създай Web Service:**
1. След login, кликни **"New +"** (горе вдясно)
2. Избери **"Web Service"**
3. Кликни **"Connect account"** ако не е свързан GitHub
4. Намери **`cbt-docx-processor`** repo
5. Кликни **"Connect"**

### **В) Настройки:**

**Settings:**
- **Name:** `cbt-docx-processor`
- **Region:** `Frankfurt (EU Central)` (по-близо до България)
- **Branch:** `main`
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

**Instance Type:**
- Избери **"Free"** (0$/month)

### **Г) Environment Variables:**
Няма нужда от променливи за момента.

### **Д) Deploy:**
1. Скролни до края
2. Кликни **"Create Web Service"**
3. Render започва deploy (отнема 2-3 минути)
4. Виж лог-овете - трябва да завърши със "Your service is live"

---

## СТЪПКА 3: Копирай API URL (1 мин)

След успешен deploy:

1. В Render dashboard виж URL-а на сървиса:
   ```
   https://cbt-docx-processor.onrender.com
   ```
2. **КОПИРАЙ този URL** - ще ти трябва за Make.com!

---

## СТЪПКА 4: Тестване (2 мин)

### **А) Health Check:**
Отвори в браузър:
```
https://cbt-docx-processor.onrender.com/
```

Трябва да видиш:
```json
{
  "status": "online",
  "message": "CBT DOCX Processor API",
  "endpoints": {
    "/process-docx": "POST - Process DOCX with replacements"
  }
}
```

### **Б) Test endpoint (optional):**
Ако искаш да тестваш с cURL:

```bash
curl -X POST https://cbt-docx-processor.onrender.com/process-docx \
  -F "file=@Protokol_2_Template.docx" \
  -F 'replacements={"{{stroej}}":"Тестова сграда"}' \
  --output test_result.docx
```

---

## ✅ Готово!

API-то е live на: `https://cbt-docx-processor.onrender.com`

---

## 🔧 Важни бележки:

### **Free tier ограничения:**
- Сървърът "заспива" след 15 мин неактивност
- Първото request след "заспиване" отнема 30-60 секунди
- След това работи нормално
- 750 часа безплатно на месец (достатъчно)

### **Ако има проблеми:**
1. Провери лог-овете в Render dashboard
2. Уверѝ се че всички файлове са upload-нати в GitHub
3. Провери Build Command и Start Command

---

## 📋 Следващи стъпки:

След като API-то работи:
1. ✅ Копирай URL-а
2. ✅ Отиди в Make.com
3. ✅ Създай сценарий с HTTP модул към този URL

---

## 🐛 Troubleshooting:

**"Build failed":**
- Провери дали `requirements.txt` е качен
- Провери дали `.python-version` съществува

**"Application failed to start":**
- Провери Start Command: `gunicorn app:app`
- Виж лог-овете за грешки

**"502 Bad Gateway":**
- Изчакай 1-2 минути - deploy-ва се
- Refresh страницата

---

## 📞 Помощ:

Ако имаш проблеми на някоя стъпка - изпрати ми screenshot и веднага ще помогна! 🚀
