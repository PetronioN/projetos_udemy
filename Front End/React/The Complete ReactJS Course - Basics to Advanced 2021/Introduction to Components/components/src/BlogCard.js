import React from 'react';

import { dumpLogs } from './Utils';

// import './BlogCard.css';
import classes from './BlogCard.module.css';

const BlogCard = (props) => {
    dumpLogs(props);

	console.log(props.key) // essas propriedades irão virar objetos
	return (
		<div className={classes.NewBlogCard}>
			<h3>{props.title}</h3>
			<p>{props.description}</p>
		</div>
	)
}

export default BlogCard;