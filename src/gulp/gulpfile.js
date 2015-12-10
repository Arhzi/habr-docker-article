/**
 * Created by werevolff on 18.10.15.
 */

var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat'),
    refresh = require('gulp-livereload'),
    lr = require('tiny-lr'),
    server = lr();


/**
 * Mainpage
 */
gulp.task('mainpage', function () {
    gulp.src(['./front/jquery/*.js', './front/bootstrap/*.js', './front/angularjs/angular.min.js',
        './front/angularjs/i18n/angular-locale_ru-ru.js', './front/project/**/*.js'])
        .pipe(uglify())
        .pipe(concat('mainpage.js'))
        .pipe(gulp.dest('./build'))
        .pipe(refresh(server));
});


/**
 * Rebuild JS files
 */

gulp.task('lr-server', function () {
    server.listen(35729, function (err) {
        if (err) return console.log(err);
    });
});

/**
 * Gulp Tasks
 */
gulp.task('default', ['mainpage', 'lr-server'], function () {
    gulp.watch('./front/**/*.js', ['mainpage']);
});