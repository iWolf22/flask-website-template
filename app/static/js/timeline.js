document.addEventListener("DOMContentLoaded", function () {
	const form = document.getElementById("timeline-form");
	const postsContainer = document.getElementById("timeline-posts");

	async function fetchPosts() {
		const res = await fetch("/api/timeline_post");
		const data = await res.json();
		postsContainer.innerHTML = "";
		if (data.timeline_posts && data.timeline_posts.length > 0) {
			data.timeline_posts.forEach((post) => {
				const postDiv = document.createElement("div");
				console.log(post);
				postDiv.className = "timeline-post";
				postDiv.innerHTML = `
                    <div class="timeline-post-header">
                        <span class="timeline-post-name">${post.name}</span>
                        <span class="timeline-post-email">${post.email}</span>
                        <span class="timeline-post-date">${new Date(
							post.created_at
						).toLocaleString()}</span>
                    </div>
                    <div class="timeline-post-content">${post.content}</div>
                `;
				postsContainer.appendChild(postDiv);
			});
		} else {
			postsContainer.innerHTML = "<p>No posts yet.</p>";
		}
	}

	form.addEventListener("submit", async function (e) {
		e.preventDefault();
		const formData = new FormData(form);
		const data = new URLSearchParams(formData);
		await fetch("/api/timeline_post", {
			method: "POST",
			body: data,
		});
		form.reset();
		fetchPosts();
	});

	fetchPosts();
});
