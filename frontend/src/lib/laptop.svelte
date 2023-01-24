<script lang="ts">
	import type { Laptop } from 'src/types/types';
	import { quintInOut } from 'svelte/easing';
	import { crossfade } from 'svelte/transition';

	const [send, receive] = crossfade({
		duration: (d) => Math.sqrt(d * 200),

		fallback(node, params) {
			const style = getComputedStyle(node);
			const transform = style.transform === 'none' ? '' : style.transform;

			return {
				duration: 600,
				easing: quintInOut,
				css: (t) => `
					transform: ${transform} scale(${t});
					opacity: ${t}
				`
			};
		}
	});

	export let laptop: Laptop;
</script>

<div in:receive={{ key: laptop.id }} out:send={{ key: laptop.id }}>
	<img src="./{laptop.os}{laptop.id % 3}.jpg" alt="laptop" />
	<h5>{laptop.manufacturer} {laptop.model_name}</h5>
	<h6>₹ {laptop.price}</h6>
</div>

<style>
	div {
		display: grid;

		place-items: center;

		background-color: #ffffffaa;
		border-radius: 5px;

		grid-template-columns: 1fr 1fr;
		grid-template-rows: 3fr 1fr 1fr;

		grid-template-areas:
			'img img'
			'name name'
			'price price';
	}

	img {
		margin-top: 0;
		padding-top: 0;
		grid-area: img;
		align-self: center center;
		width: 100%;
		border-radius: 5px;
		object-fit: cover;
	}
	div > h5 {
		grid-area: name;
		align-self: center left;
		font-size: x-large;
	}
	div > h6 {
		grid-area: price;
		text-align: left;
		font-size: larger;
		color: #888;
	}
</style>
